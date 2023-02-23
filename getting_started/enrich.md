## Enrich

The `enrich` module provides a number of enrichments of the `Dash` object that can be enabled in a modular fashion. To get started, replace imports from `Dash` with imports from `dash_extensions.enrich`,

```python
from dash import Input, Output, html, ...  # before
from dash_extensions.enrich import Input, Output, html, ...  # after
```

and exchange the `Dash` object with a `DashProxy` object with the desired transforms enabled,

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

The `enrich` module also exposes a `Dash` object, which is a `DashProxy` object with all transforms loaded, i.e. a batteries included approach. However, it is recommended to load only the transforms are that actually used.

The transforms are documented in detail on separate pages (see the **Transforms** section in the menu to the left), while underlying framework is documented below. The framework documentation is not limited to technical details. It covers also practical applications of the `enrich` module functionality, such as modular Dash application development, and how to get started developing your own transforms. Hence, to get the most of the `enrich` module, it is recommended to keep reading.

### DashBlueprint

Inspired by [Flask blueprints](https://flask.palletsprojects.com/en/2.1.x/blueprints/), the `enrich` module introduces the concept of blueprints in a Dash context via the `DashBlueprint` object. It 
encapsulates a Dash layout along with associated callbacks, thus enabling modular Dash application development. The syntax for creating a blueprint is the same as for regular Dash applications,

```python
from dash_extensions.enrich import DashBlueprint, html, Output, Input

bp = DashBlueprint()
bp.layout = html.Div([html.Button('Click me!', id='btn'), html.Div(id='log')])

@bp.callback(Output('log', 'children'), Input('btn', 'n_clicks'))
def on_click(n_clicks):
    return f"Hello world {n_clicks}!"
```

Since blueprints do not reference the Dash application object, they can be defined in files separate from the Dash application. Or even in a different library. The most common ways to bring a blueprint to life are by

* Turning it into a Dash application via the [`DashProxy` object](#a-dashproxy)
* [Embedding](#a-embedding) it in an existing Dash application
* Registering it [as a page](#a-pages) in an existing Dash application using [pages](https://dash.plotly.com/urls)

To avoid id collisions between blueprints, _id prefixing_ is supported via the `PrefixIdTransform`. Hence, it is possible to use blueprints with the same ids in the same application; or even use the same blueprint multiple times.

#### DashProxy

The `DashProxy` object is a thin wrapper around `DashBlueprint` that turns it into a drop-in replacement for the `dash.Dash` application object,

.. python-code:: getting_started.dash_proxy

Like the (raw) `DashBlueprint` object, the `DashProxy` object supports [transforms](#a-dashtransform).

#### Embedding

To embed a blueprint in a Dash application, use the `embed` function. It transfers the callbacks from the blueprint to the Dash app, and returns the resulting layout,

.. python-code:: getting_started.embedding

As it is possible to embed any number of blueprints, this strategy can be used to modularize the Dash application development.

#### Pages

Using the embedding approach described above, it is possible to register blueprints as separate pages in a multipage application setup, but it requires a bit of code. If you are using the [pages](https://dash.plotly.com/urls), the process is streamlined via the `register` function,

.. python-code:: getting_started.pages

Note that because the pages are registered with different values for the `prefix` argument, each page works even though the component ids are overlapping.

### DashTransform

A `DashTransform` represents a _transformation_ of one `DashBlueprint` into another. Since a blueprint holds both callback and layout information, transforms can make arbitrary modifications of both. Transforms can be passed via the `transforms` keyword of `DashBlueprint` and/or `DashProxy`. The key purpose of transforms is to make it possible to encapsulate blocks of application logic, and abstract it away. 

As a simple example, let's consider the case of callbacks that are invoked only for their side effects. A typical example is executing a small JavaScript snippet. In Dash, a callback _must_ have an output, so the workaround for this case would be to add a dummy output,

.. python-code:: getting_started.side_effect

While this code _works_, it is not very elegant. Now, let's think about how the syntax _should_ be. 
The simplest would probably be just to omit the output all together. The required steps to turn this desired syntax into valid Dash syntax would be to

* Identify all callbacks that have no outputs
* For each of these callbacks, create a dummy output element, and add it to the application layout
* For each of these callbacks, assign the respective dummy element as the output

The steps above defines a _transformation_ of one `DashBlueprint` into another, and can thus be implemented as a `DashTransform`. Using the resulting `NoOutputTransform` (if you are interested in the details, take a look at the [source code](https://github.com/thedirtyfew/dash-extensions/blob/master/dash_extensions/enrich.py)), the previous example can be written as,

.. python-code:: getting_started.side_effect_transform

### CeleryManager

For the `CeleryManager` (used with [background callbacks](https://dash.plotly.com/background-callbacks)) to pickup background callbacks, an explicit registration of callbacks must be performed. This can be done by adding the following line,

    app.register_celery_tasks()

at the end of the main application file (where `app` is the `DashProxy` object). Additionally, the Celery worker process must be started manually in a separate process. This can be done by invoking the following command in a separate terminal,

     celery -A my_app.celery_app worker

where `my_app` is the name of the main application file, and `celery_app` is the variable name of the Celery app within that file.

### Known limitations

* Transforms do not support the (deprecated) `long_callback` decorator, but the newer syntax using the standard `callback` decorator with keyword argument `background=True` is supported from version 0.1.6, see [the official docs](https://dash.plotly.com/background-callbacks) for details