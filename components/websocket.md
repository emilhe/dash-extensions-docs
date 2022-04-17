### WebSocket

The `WebSocket` component enables communication via _websockets_ in Dash. As compared to HTTP, the websocket protocol provides lower latency, and bidirectional capabilities, and it is thus better suited for use cases such as real time updates and push notification. 

##### Real-time data streaming

As a first example, consider a scenario where you want to stream data in real time. It could be from a sensor, a data processing pipeline, or something different; the data origin is not important. For simplicity, let's consider a [Quart](https://pgjones.gitlab.io/quart/) server that emits 10 random numbers every second,

.. python:: components.websocket_streaming_server

Including a `WebSocket` component (with the `url` property set to match the websocket endpoint) in the layout of a Dash app, one can stream the data via a callback attached to the `message` property. Here is a small Dash app, that plots the emitted data in real time,

.. python:: components.websocket_streaming_client

A client-side callback has been used to optimize performance, but normal callbacks will work too.

##### Low latency communication 

As the websocket protocol is bidirectional, it is also possible to send data to the server. This can be done via the `send` property. As a simple example, consider the following app,

.. python:: components.websocket_client

Here, a text input is sent via the websocket in the `send` callback, and the processed message is read in `message` callback, and printed to the log. A corresponding echo server implementation (i.e. a server that just returns the message received) in Quart would be,

.. python:: components.websocket_server

##### Notes

To run the example(s) above, it is recommended to start the server in one terminal, and the app in another. 

.. api-doc:: dash_extensions.WebSocket