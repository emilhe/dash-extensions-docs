The `dash-extensions` package can be divided in four main pillars,

* The [`enrich` module](), which contains various enriched versions of Dash components
* A number of custom components, e.g. the `Websocket` component, which enables real-time communication
* The [`javascript` module](), which contains functionality to ease the interplay between Dash and JavaScript
* The `snippets` module, which contains a collection of utility functions (documentation limited to source code comments)

The `enrich` module enables a number of _transforms_ that add functionality and/or syntactic sugar. Examples include

* Making it possible to target an `Output` by multiple callbacks via the [MultiplexerTransform]()
* Enabling logging from within Dash callbacks via the [LogTransform]()
* Improving app performance via the [ServersideOutputTransform]()

When possible, the usage of transforms and custom Dash components is illustrated via one (or more) code examples with the actual code running below. Hence, it should be possible to copy-paste the code and run it right away.