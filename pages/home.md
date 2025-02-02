The `dash-extensions` package holds mixture of Dash components and Python modules. Here is a brief overview,
* The [`enrich` module](sections/enrich), which contains various enriched versions of Dash components
* A number of custom components, e.g. the [`Websocket` component](components/websocket), which enables push notifications and real-time communication
* The [`javascript` module](sections/javascript), which contains functionality to ease the interplay between Dash and JavaScript
* The [`logging` module](sections/logging), which makes it a breeze to route logs to your Dash UI
* The [`pages` module](sections/pages), which extends the functionality of [Dash Pages](https://dash.plotly.com/urls)
* The `snippets/validation` modules, which contain a collection of utility functions (documentation limited to source code comments)

The `enrich` module enables a number of _transforms_ that add functionality and/or syntactic sugar to Dash. Examples include

* Making it possible to avoid invoking a callback _if it is already running_ via the [`BlockingCallbackTransform`](transforms/blocking_callback_transform)
* Improving app performance via the [`ServersideOutputTransform`](transforms/serverside_output_transform)
* Automated serialization/deserialization of [Pydantic](https://docs.pydantic.dev/latest/) models via the [`BaseModelTransform`](transforms/base_model_transform)

When possible, the usage of transforms and custom Dash components is illustrated via one (or more) code examples with the actual code running below. Hence, it should be possible to copy-paste the code and run it right away.