## Keyboard

The `Keyboard` component makes it possible to listen to keyboard events. Simply wrap the relevant component(s) in an `Keyboard` component, specify which key(s) to capture, and what event properties to send back to Dash,

.. dash-proxy:: components.keyboard

If the `Keyboard` component has no children, it will instead attach to the root document. This is useful if you want to listen to keyboard events globally.

.. api-doc:: dash_extensions.EventListener



