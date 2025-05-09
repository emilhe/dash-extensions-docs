## Migration

The page contains migration guidelines for releases that contain breaking changes.

### 2.0.0

The new version targets Dash 3. While things may work with older Dash versions, it is not guaranteed. Tests are run against Dash 3 only. It is recommended to update to `dash==3.0.2` or later.

The interface of the `Lottie` was changed slightly, e.g. you can no longer pass style arguments such as `width` directly. Instead, they must be set as part of the `style` dict in the `options` property. Please refer to the [documentation](/components/lottie) for additional details.

The `LogTransform` was removed. Please use the [logging` module](/sections/logging) instead.

The `NoOuputTransform` was removed. As per Dash 2.17.0, callbacks with outputs are supported out of the box. Hence, no migration is necessary (apart from removing the `NoOuputTransform` itself).

The `dataiku` module was removed. With Dataiku being a proprietary platform that i no longer have access to, I am not able to provide guidelines on possible migration strategies.

### 1.0.0

The `OperatorTransform` was removed. The recommended migration approach is to switch to [partial property updates](https://dash.plotly.com/partial-properties) introduced in Dash 2.9, which offer similar functionality.

The `MultiplexerTransform` was refactored to take advantage of the native implementation introduced in Dash 2.9. No code changes should be necessary, but it should be noted that support for pattern matching callbacks is now available.

The `ServersideOuputTransform` has been refactored. The initialization syntax has changed slightly, and instead of replacing an `Output` by `ServersideOutput`, one must now wrap the return value in a `Serverside` component (see [the separate documentaion section](/transforms/serverside_output_transform) for details). A benefit of this change in syntax is that it is now possible to change between saving data on the server and the client for different callbacks; or for different code paths inside the same callback. It should also be noted that support for pattern maching callbacks has been improved.
