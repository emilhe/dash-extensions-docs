## LogTransform

The `LogTransform` makes it possible to direct logs to a Dash component. When `log=True` is passed as a keyword argument to a callback, a `DashLogger` object is passed to the callback as the last argument. Here is a small example,

.. dash-proxy:: transforms.log_transform

The component to which the logs are sent as well as the log formatting can be customized by passing a `LogConfig` object to the `LogTransform`. Per default, the [dash-mantine-components](https://github.com/snehilvj/dash-mantine-components) notification system is used if the library is available, otherwise logs are directed to a `Div` element, which is appended to the layout. 



