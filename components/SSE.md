## SSE

The `SSE` component makes it possible to send data _from the server_ (unidirectional) to a Dash application. The `SSE` component can thus be considered as an alternative to the `WebSocket` component for cases where bidirectional communication is not needed.

### Real-time data streaming

As an example, consider a scenario where you want to stream data in real time. It could be from a sensor, a data processing pipeline, the output of a large language model or something different; the data origin is not important. For simplicity, let's consider a [FastAPI](https://fastapi.tiangolo.com/) server that streams back the message that it received,

.. python-code:: components.sse_server

The definition of `MyModel` is simply,

.. python-code:: components.sse_model

Including an `SSE` component in the layout of a Dash app, the streaming is initiated when the `url` (and optionally the `options` property) is set. In the example below, a button is used as trigger, and the resulting data (i.e. the `value`) is logged to `Div`, 

<!-- .. python-code:: components.event_source_client -->

### Notes

To run the example(s) above, it is recommended to start the server in one terminal, and the app in another. 

.. api-doc:: dash_extensions.SSE