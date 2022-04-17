### NoOutputTransform

The `NoOutputTransform` makes it possible to create callbacks without an `Output`. Here is a small example,

.. dash-proxy:: transforms.no_output_transform

Technically, the `NoOutputTransform` works by assigning dummy output elements to callbacks without outputs. The dummy elements are appended to the app layout.