## Migration

The page contains migration guidelines for releases that contain breaking changes.

### 1.0.0

The `OperatorTransform` was removed. The recommended migration approach is to switch to [partial property updates](https://dash.plotly.com/partial-properties) introduced in Dash 2.9, which offer similar functionality.
 
The `MultiplexerTransform` was refactored to take advantage of the native implementation introduced in Dash 2.9. No code changes should be necessary, but it should be noted that support for pattern matching callbacks is now available. 

The `ServersideOuputTransform` has been refactored. The initialization syntax has changed slightly, and instead of replacing an `Output` by `ServersideOutput`, one must now wrap the return value in a `Serverside` component (see [the separate documentaion section](/transforms/serverside_output_transform) for details). A benefit of this change in syntax is that it is now possible to change between saving data on the server and the client for different callbacks; or for different code paths inside the same callback. It should also be noted that support for pattern maching callbacks has been improved.