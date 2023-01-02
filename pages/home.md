The `dash-extensions` package can be divided in four main pillars,

* The [`enrich` module](getting_started/enrich), which contains various enriched versions of Dash components
* A number of custom components, e.g. the [`Websocket` component](components/websocket), which enables push notifications and real-time communication
* The [`javascript` module](getting_started/javascript), which contains functionality to ease the interplay between Dash and JavaScript
* The `snippets` module, which contains a collection of utility functions (documentation limited to source code comments)

The `enrich` module enables a number of _transforms_ that add functionality and/or syntactic sugar to Dash. Examples include

* Making it possible to target an `Output` by multiple callbacks via the [MultiplexerTransform](transforms/multiplexer_transform)
* Enabling logging from within Dash callbacks via the [LogTransform](transforms/log_transform)
* Improving app performance via the [ServersideOutputTransform](transforms/serverside_output_transform)

When possible, the usage of transforms and custom Dash components is illustrated via one (or more) code examples with the actual code running below. Hence, it should be possible to copy-paste the code and run it right away.