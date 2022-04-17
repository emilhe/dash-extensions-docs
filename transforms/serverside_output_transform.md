### ServersideOutputTransform

The `ServersideOutputTransform` makes it possible to use the `ServersideOutput` component. It works like a normal `Output`, but _keeps the data on the server_. By skipping the data transfer between server/client, the network overhead is reduced drastically, and the serialization to JSON can be avoided. Hence, you can now return complex objects, such as a Pandas data frame, directly. Here is a small example,

.. dash-proxy:: transforms.serverside_output_transform

The reduced network overhead along with the avoided serialization to/from JSON can yield **significant** performance improvements, in particular for large data. Note that content of a `ServersideOutput` cannot be accessed by clientside callbacks.

##### Backends

The `ServersideOutputTransform` stores the callback output data in a _backend_ on the server. The default backend is a `FileSystemStore`, which simply dumps the data on disk (per default, in a folder called `file_system_store`) using the `pickle` protocol. Other backends can be passed via the `backend` keyword argument,

```python
my_backend = FileSystemStore(cache_dir="some_dir")

...

@app.callback(ServersideOutput("store", "data", backend=my_backend), Input("btn", "n_clicks"), memoize=True)
def query_data(n_clicks):
    ...
```

In addition to the `FileSystemStore`, a `RedisStore` is also available that binds to a Redis server. If you need other storage options, t is straight forward to implement a new backend using other storage options. Just create a new class that implements the following interface,

```python
def get(self, key, ignore_expired=False) -> any:
    ...
```

If `ignore_expired=True`, the function **must** return the value, even if it has been marked as expired in the cache. Some caches perform cleanup internally (e.g. Redis), in which case the timeout must be set high enough that the cache _never expires during a user session_. That's why the default timeout value for the `RedisStore` is set to 24 hours.

##### Backend cleanup

The default `FileSystemStore` doesn't include any clean up mechanism. Hence, the caching directory (per default `file_system_store`) will grow in size indefinitely as the app is used. If space is an issue, it is recommended to perform scheduled cleanups outside business hours, e.g. every night a 3 am. Other backends (e.g. Redis) performs the cleanup automatically.

##### Memoization

A `memoize` keyword makes it possible to memoize the output of a callback. That is, the callback output is cached, and the cached result is returned when the same inputs occur again. Used with a normal `Output`, this keyword is essentially equivalent to the `@flask_caching.memoize` decorator. For a `ServersideOutput`, the backend to do server side storage will also be used for memoization. Hence, you avoid saving each object two times, which would happen if the `@flask_caching.memoize` decorator was used with a `ServersideOutput`.

Now, say that we want to use memoization in the previous example to avoid the expensive (emulated) database call on subsequent clicks on the query button. If you just pass the keyword,

```python
@app.callback(ServersideOutput("store", "data"), Input("btn", "n_clicks"), memoize=True)
def query_data(n_clicks):
    ...
```

and rerun the example, you might be disappointed to see that the data is still loaded on every click. This is because the callback arguments (i.e. `n_clicks`) _changes_ at each click. The argument check can be disabled via the `arg_check` keyword,

```python
@app.callback(ServersideOutput("store", "data", arg_check=False), Input("btn", "n_clicks"), memoize=True)
def query_data(n_clicks):
    ...
```

With this change, the data should now load fast on subsequent clicks. Per default, memoization is _not shared between sessions_, but this behaviour can be changed via the `session_check` keyword,

```python
@app.callback(ServersideOutput("store", "data", arg_check=False, session_check=False), Input("btn", "n_clicks"), memoize=True)
def query_data(n_clicks):
    ...
```

If many clients are querying the same data, it might improve performance to share the cache. 

##### Global configuration

In the examples above, the customizations were applied at the callback level. It is also possible to change the default behavior by passing arguments at the transform level,

```python
app = DashProxy(transforms=[ServersideOutputTransform(backend=session_check=False, arg_check=False)])
```

##### Benchmarks

As noted previously, the `ServersideOutput` can improve performance in cases where data need to be stored/shared between callback invocations. To quantify the performance implications, a simple app was implemented where a data frame with a single column of size `n` is created server side (to emulate e.g. a fetch from a database) and inserted into a `Store` component with id `store`. Next, the mean of the column is calculated (to emulate a data processing step) in another callback that takes the store as `Input`.

The benchmark metric is chosen as the time from just after the data frame creation until just before the mean operation, i.e. it includes serialization as well as the transfer of data from the server to the client and back. For each value of `n`, 5 times measurements were carried out. The plots show the resulting average values (and std for error bars). Here are the numbers for my local desktop,

<img src="/assets/serverside_local.png" width="1200" class="center">

The left panel shows that the standard output (blue) works up til around 1 mio. rows, at which point the operation takes roughly 4s. At 10 mio. rows, the browser crashes. The serverside output (yellow) yields a consistently stable performance. I stopped at 1 bil. rows, at which point the operation took around 20s (and the pickle on disk was 8GB).

The right panel illustrates the ratio between the runtimes. Rather surprisingly to me, the serverside output is around 50 times faster for a single element data frame. Maybe this is due to the pandas serialization to/from JSON being slow? At 1 mio. rows, the cached callback is more than 200 (!) times faster. 

Now, this is fun and all, but no one uses their local host for deployment. So let’s move to the cloud (Heroku, free tier),

<img src="/assets/serverside_heroku.png" width="1200" class="center">

On Heroku, the standard output (blue) still works up til around 1 mio. rows, but the serverside output (yellow) crashed at 100 mio. rows. From the logs, I could see that the dyno ran out of memory, i.e. the limit can probably be pushed (much) further by purchasing a more beefy dyno. In the head-to-head comparison, the serverside output callback is still faster, but the performance gain has been reduced to a factor of around 10 for small data frames, and 100 for large ones.

