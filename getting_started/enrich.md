The `enrich` module provides a number of enrichment's of the `Dash` object that can be enabled in a modular fashion. To get started, replace the `Dash` object by a `DashProxy` object and pass the desired transformations via the `transforms` keyword argument, 

```python
from dash_extensions.enrich import DashProxy, TriggerTransform, MultiplexerTransform, ServersideOutputTransform, NoOutputTransform, BlockingCallbackTransform, LogTransform

app = DashProxy(transforms=[
    TriggerTransform(),  # enable use of Trigger objects
    MultiplexerTransform(),  # makes it possible to target an output multiple times in callbacks
    ServersideOutputTransform(),  # enable use of ServersideOutput objects
    NoOutputTransform(),  # enable callbacks without output
    BlockingCallbackTransform(),  # makes it possible to skip callback invocations while a callback is running 
    LogTransform()  # makes it possible to write log messages to a Dash component
])
```

The `enrich` module also exposes a `Dash` object, which is a `DashProxy` object with all transformations loaded, i.e. a batteries included approach. However, it is recommended to load only the transforms are that actually used.

NB: Transforms are not (yet) compatible the `long_callback` decorator.
