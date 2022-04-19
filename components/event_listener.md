## EventListener

The `EventListener` component makes it possible to listen to (arbitrary) JavaScript events. Simply wrap the relevant components in an `EventListener` component, specify which event(s) to subscribe to, and what event properties to send back to Dash,

.. dash-proxy:: components.event_listener

If you are not sure what properties are available/what properties you need, you can pass `logging=True` to the `EventListener` component to print the event object tree to the JavaScript console. For the example above, the Chrome developer console output would be,

<img src="/assets/event_listener.jpeg" width="800" class="center">

Note that if the relevant events are already exposed as properties in Dash, there is no benefit of using the `EventListener` component. The intended usage of the `EventListener` component is when this is _not_ the case. Say that you need to listen to double-click events, but the Dash component only exposes a (single) click property; or some data that you need is not propagated from the JavaScript layer. In these cases, the `EventListener` component makes it possible to achieve the desired behaviour without editing the component source code (i.e. the JavaScript code).

.. api-doc:: dash_extensions.EventListener



