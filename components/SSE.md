## SSE

The `SSE` component makes it possible to send data _from the server_ (unidirectional) to a Dash application. The `SSE` component can thus be considered as an alternative to the `WebSocket` component for cases where bidirectional communication is not needed.

### Real-time data streaming

As an example, consider a scenario where you want to stream data in real time. It could be from a sensor, a data processing pipeline, the output of a large language model or something different; the data origin is not important. Including an `SSE` component in the layout of a Dash app, the streaming is initiated when the `url` (and optionally the `options` property) is set. In the example below, a button is used as trigger, and the resulting data (i.e. the `value`) is logged to `Div`,

.. dash-proxy:: components.sse

For simplicity, the Flask server already running Dash was used to do the streaming. Note that the Flask development server does not support streaming, so you'll need to use gunicorn (or similar) to run the example above. Furthermore, for production workloads, it is recommended to use an async server, e.g. [FastAPI](https://fastapi.tiangolo.com/). Alternatively it is possible to run Flask using [gevent](https://flask.palletsprojects.com/en/stable/deploying/gevent/), or as a last resort use (a lot of) threads.

.. api-doc:: dash_extensions.SSE
