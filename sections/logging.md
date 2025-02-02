## Logging

The `logging` module, which replaces the deprecated `LogTransform`, provides an easy way to propagate log messages to the Dash UI.

### DashLogHandler

The `DashLogHandler` class provides a template for implementing log handlers that fit in the Python logging framework, but where the output is rendered as part of the Dash UI. Simply provide it with a Dash `Output` (where you want to logs to go), and a `dict` specifying how to render each log level, and it will take care of the rest.

### DivLogHandler

The `DivLogHandler` implements the simplest possible form of logging; writing the log text directly to a `Div`. While it can be used directly, it was mainly intended to serve as a (simple) reference implementation. Here is an example of how it can be used,

.. dash-proxy:: sections.logging.divloghandler

Note that the `embed()` call returns any components created by the log handler to be inserted into the app layout. For the `DivLogHandler` that's just a `Div`. It is also possible to create the `Div` manually, and pass it to the `DivLogHandler`. Something like,

```python
...
app.layout = html.Div(..., log_div := html.Div(id="log_id")]
)

log_handler = DivLogHandler(log_div)
logger = log_handler.setup_logger()
...
```

### NotificationsLogHandler

The `NotificationsLogHandler`uses the notifications system from [Dash Mantine Components](https://www.dash-mantine-components.com/) (dmc) to display log messages. As compared to the previous example, we can (almost) do a drop-in replacement,

.. dash-proxy:: sections.logging.notificationsloghandler

The only additional changes required are to wrap the layout in `MantineProvider` (a general requirement to use dmc) and to add the appropriate CSS styles.