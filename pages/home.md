The `dash-extensions` package can be divided in five main pillars,

* The [`enrich` module](sections/enrich), which contains various enriched versions of Dash components
* A number of custom components, e.g. the [`Websocket` component](components/websocket), which enables push notifications and real-time communication
* The [`javascript` module](sections/javascript), which contains functionality to ease the interplay between Dash and JavaScript
* The [`pages` module](sections/pages), which extends the functionality of [Dash Pages](https://dash.plotly.com/urls)
* The `snippets/validation` modules, which contain a collection of utility functions (documentation limited to source code comments)

The `enrich` module enables a number of _transforms_ that add functionality and/or syntactic sugar to Dash. Examples include

* Making it possible to avoid invoking a callback _if it is already running_ via the [`BlockingCallbackTransform`](transforms/blocking_callback_transform)
* Enabling logging from within Dash callbacks via the [`LogTransform`](transforms/log_transform)
* Improving app performance via the [`ServersideOutputTransform`](transforms/serverside_output_transform)

When possible, the usage of transforms and custom Dash components is illustrated via one (or more) code examples with the actual code running below. Hence, it should be possible to copy-paste the code and run it right away.