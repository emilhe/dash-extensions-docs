### WebSocket

The `WebSocket` component enables communication via _websockets_ in Dash. As compared to HTTP, the websocket protocol provides lower latency, and bidirectional capabilities, and it is thus better suited for use cases such as real time updates and push notification. 

Add the `WebSocket` component to the layout, and set the `url` property to the websocket endpoint. Messages can be send by writing to the `send` property, and received messages are written to the `message` property. As a simple example, consider the following app,

.. python:: components.websocket_client

where a text input is sent via the websocket in the `send` callback. Similarly, the `message` callback receives messages sent by the server and prints them to the log. To complete the example, a websocket server implementation is need. For simplicity here is an example in Python using Quart, 

.. python:: components.websocket_server

which just echos the message received back to the sender.

<br>

.. api-doc:: dash_extensions.WebSocket


