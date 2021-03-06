## MultiplexerTransform

The `MultiplexerTransform` makes it possible to target an output by multiple callbacks. Here is a small example,

.. dash-proxy:: transforms.multiplexer_transform

Under the hood, when `n` > 1 callbacks target the same element as output, _n_ `Store` elements are created, and the callbacks are redirect to target these intermediate outputs. Finally, a callback is added with the intermediate outputs as inputs and the original output as output. The strategy was contributed by [dwelch91](https://community.plotly.com/u/dwelch91/summary).

### Wrappers, e.g. dcc.Loading

Since the `MultiplexerTransform` modifies the original callback to target a proxy component, wrappers (such as the `Loading` component) targeting the original output will not work as intended. If the output is static (i.e. not recreated by callbacks), the issue can be avoided by injecting the proxy component next to the original output in the component tree,

```python
app = DashProxy(transforms=[MultiplexerTransform(proxy_location="inplace")])
```

If the output is not static, the recommended mitigation strategy is not to wrap to original output object, but to instead pass the wrapper(s) as proxy component wrappers,

```python
proxy_wrapper_map = {Output("log0", "children"): lambda proxy: dcc.Loading(proxy, type="dot")}
app = DashProxy(transforms=[MultiplexerTransform(proxy_wrapper_map)])
```

### Know limitations

The `MultiplexerTransform` does not support the `MATCH` and `ALLSMALLER` wildcards. The `MultiplexerTransform` does not support `ServersideOutput`.