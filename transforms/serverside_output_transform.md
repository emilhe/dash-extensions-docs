## ServersideOutputTransform

The `ServersideOutputTransform` makes it possible to use the `Serverside` component. When a callback return value is wrapped `Serverside` component, the data is _kept on the server_. By skipping the data transfer between server/client, the network overhead is reduced drastically, and the serialization to JSON can be avoided. Hence, you can now return complex objects, such as a Pandas data frame, directly. Here is a small example,

.. dash-proxy:: transforms.serverside_output_transform

The reduced network overhead along with the avoided serialization to/from JSON can yield **significant** performance improvements, in particular for large data.

### Backends

The `ServersideOutputTransform` stores the callback output data in a _backend_ on the server. The default backend is a `FileSystemBackend`, which simply dumps the data on disk (per default, in a folder called `file_system_backend`) using the `pickle` protocol. Custom backends can be registered via the `backends` keyword argument of the transform, 

```python
one_backend = FileSystemBackend("one_backend")
another_backend = FileSystemBackend("another_backend")
app = DashProxy(transforms=[ServersideOutputTransform(backends=[one_backend, another_backend])])
```

If multiple backends are registered, the default can be specified via the `default_backend` keyword argument. If not specified, the first element in the list (here `one_backend`) will be used as default. To use a particular backend, specify it via the `backend` keyword argument of `Serverside`,

```
@app.callback(...)
def some_callback(n_clicks):
    ...
    return Serverside(..., backend=another_backend)
```

In addition to the `FileSystemBackend`, a `RedisBackend` is available that binds to a Redis server. If you need other storage options, it is straight forward to implement a new backend using other storage options. Just create a new class that implements the following interface,

```python
def get(self, key, ignore_expired=False) -> any:
    ...
```

If `ignore_expired=True`, the function **must** return the value, even if it has been marked as expired in the cache. Some caches perform cleanup internally (e.g. Redis), in which case the timeout must be set high enough that the cache _never expires during a user session_. That's why the default timeout value for the `RedisStore` is set to 24 hours.

### Backend cleanup

The default `FileSystemBackend` doesn't include any clean up mechanism. Hence, the caching directory (per default `file_system_backend`) will grow in size indefinitely as the app is used. If space is an issue, it is recommended to perform scheduled cleanups outside business hours, I typically do it every night at 3 am. Other backends (e.g. Redis) performs the cleanup automatically.

### Benchmarks

As noted previously, the `Serverside` component can improve performance in cases where data need to be stored/shared between callback invocations. To quantify the performance implications, a simple app was implemented where a data frame with a single column of size `n` is created serverside (to emulate e.g. a fetch from a database) and inserted into a `Store` component with id `store`. Next, the mean of the column is calculated (to emulate a data processing step) in another callback that takes the store as `Input`.

The benchmark metric is chosen as the time from just after the data frame creation until just before the mean operation, i.e. it includes serialization as well as the transfer of data from the server to the client and back. For each value of `n`, 5 times measurements were carried out. The plots show the resulting average values (and std for error bars). Here are the numbers for my local desktop,

<img src="/assets/serverside_local.png" width="1200" class="center">

The left panel shows that the standard output (blue) works up til around 1 mio. rows, at which point the operation takes roughly 4s. At 10 mio. rows, the browser crashes. The serverside  (yellow) yields a consistently stable performance. I stopped at 1 bil. rows, at which point the operation took around 20s (and the pickle on disk was 8GB).

The right panel illustrates the ratio between the runtimes. Rather surprisingly to me, the serverside approach is around 50 times faster for a single element data frame. Maybe this is due to the pandas serialization to/from JSON being slow? At 1 mio. rows, the cached callback is more than 200 (!) times faster. 

Now, this is fun and all, but no one uses their local host for deployment. So let’s move to the cloud (Heroku, free tier),

<img src="/assets/serverside_heroku.png" width="1200" class="center">

On Heroku, the standard approach (blue) still works up til around 1 mio. rows, while the serverside approach (yellow) crashed at 100 mio. rows. From the logs, I could see that the dyno ran out of memory, i.e. the limit can probably be pushed (much) further by purchasing a more beefy dyno. In the head-to-head comparison, the serverside approach is still faster, but the performance gain has been reduced to a factor of around 10 for small data frames, and 100 for large ones.

It should be noted that the performance gains reported here apply only to operations where server side caching is relevant (e.g. sharing of data between callbacks). Hence, you shouldn't generally expect your app to become 100 times faster by using the `ServersideOutputTransform`. In fact, if the performance bottleneck in your app is elsewhere (e.g. rendering of large figures), it might not become faster at all.