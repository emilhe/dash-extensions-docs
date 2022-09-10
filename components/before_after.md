## BeforeAfter

The `BeforeAfter` component is a light wrapper of [img-comparison-slider](https://github.com/sneas/img-comparison-slider), which makes it easy to *highlight differences between two images*. Here is a small example,

.. dash-proxy:: components.before_after

A wide range of customization options are available as illustrated in the [usage examples](https://img-comparison-slider.sneas.io/examples.html) for the underlying component. In addition to options exposed as props directly in Dash (e.g. the `keyboard` and `direction` props), it is also possible to pass additional properties to the first/second `img` element via the `before`/`after` dict. 

.. api-doc:: dash_extensions.BeforeAfter