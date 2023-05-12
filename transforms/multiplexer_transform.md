## MultiplexerTransform

The `MultiplexerTransform` was originally designed to make it possible to target an output by multiple callbacks. As per Dash 2.9, this functionality is now [available in `dash`](https://dash.plotly.com/duplicate-callback-outputs) via the new `allow_duplicate` flag of the `Output` object. However, this flags defaults to `False`, so for backwards compatibility a new (greatly simplified) version of the `MultiplexerTransform` has been implemented, which simply changes this flag to `True` if an `Output` is used in multiple callbacks. Hence, code like in the example below, will still work,

.. dash-proxy:: transforms.multiplexer_transform