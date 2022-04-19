## TriggerTransform

The `TriggerTransform` makes it possible to use the `Trigger` component. Like an `Input`, it can trigger callbacks, but its value is not passed on to the callback. Here is a small example,

.. dash-proxy:: transforms.trigger_transform

Technically, the `TriggerTransform` works by filtering out the arguments in the Python layer of Dash. 

### Know limitations

It works only for normal callbacks, not clientside callbacks.