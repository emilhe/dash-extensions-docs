## Installation

The pages contains migration instruction for releases that contain breaking changes.

### 1.0.0

The `OperatorTransform` was removed. The recommended migration approach is to use [partial property updates](https://dash.plotly.com/partial-properties) introduced in Dash 2.9, which  similar functionality.
 
The `MultiplexerTransform` was refactored to take advantage of the native implementation introduced in Dash 2.9. No code changes should be necessary, but it should be noted that support for pattern matching callbacks is now available. 

The `ServersideOuputTransform` has been refactored. The initialization syntax has changes slightly (see the separate documentaion section for details), and instead of replacing an `Output` by `ServersideOutput`, one must now wrap the return value in a `Serverside` component instead. A benefit of this change in syntax is that it is now possible change between saving data on the server and the client for different callbacks; or for different code paths inside the same callback. It should also be noted that support for pattern maching callbacks has been improved.