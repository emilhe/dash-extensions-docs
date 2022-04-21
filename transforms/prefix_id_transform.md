## PrefixIdTransform

The `PrefixIdTransform` adds a prefix to all component ids, including their references in callbacks. It is typically used to avoid id collisions between blueprints when they are registered on/embedded in the main Dash application. Here is a small example,

.. dash-proxy:: transforms.prefix_id_transform

Note the extra "prefix_id_transform" prefix in the button id. That's because the page you are viewing is itself a `DashBlueprint` registered with a prefix equal to "prefix_id_transform".