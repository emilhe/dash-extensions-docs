## BaseModelTransform

The `BaseModelTransform` makes it possible to serialize [Pydantic](https://docs.pydantic.dev/latest/) `BaseModel` classes. Simply add a typehint for the relevant arguments, and the rest is taken care off automagically. Here is a small example,

.. dash-proxy:: transforms.base_model_transform