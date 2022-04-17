### BlockingCallbackTransform

The `BlockingCallbackTransform` makes it possible to avoid invoking a callback _if it is already running_. A typical use case is while polling data at an interval (say 1s) that is longer than the time it takes the callback to execute (say, 5s). The transform is applied per callback by passing the `blocking` flag. Here is a small example,

.. dash-proxy:: transforms.blocking_callback_transform

Under the hood, hidden dummy elements (client side) and client side callbacks keep track of whether a callback is already running or not. If it is already running, the Python callback invocation is skipped.
