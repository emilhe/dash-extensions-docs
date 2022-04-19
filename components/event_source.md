## EventSource

The `EventSource` component makes it possible to send data _from the server_ (unidirectional) to a Dash application. The `EventSource` component can thus be considered as an alternative to the `WebSocket` component for cases where bidirectional communication is not needed.

### Real-time data streaming

As an example, consider a scenario where you want to stream data in real time. It could be from a sensor, a data processing pipeline, or something different; the data origin is not important. For simplicity, let's consider a [Starlette](https://www.starlette.io/) server that emits 10 random numbers every second,

.. python-code:: components.event_source_server

Including an `EventSource` component (with the `url` property set to match the event source endpoint) in the layout of a Dash app, one can stream the data via a callback attached to the `message` property. Here is a small Dash app, that plots the emitted data in real time,

.. python-code:: components.event_source_client

### Notes

To run the example(s) above, it is recommended to start the server in one terminal, and the app in another. 

.. api-doc:: dash_extensions.EventSource

