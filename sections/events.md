## Events

The `events` module provides an event flow syntax for Dash inspired by JavaScript. The following example demonstrates its simplest form,

.. dash-proxy:: sections.events.minimal

The above syntax is intended for cases where you don't need to pass information with the event. If you do, the recommended approach is to use a Pydantic model as demonstrated in the following example,

.. dash-proxy:: sections.events.base_model

The `events` module is built on top of the `set_props` released with Dash 2.17.0, and it is there not compatible with older Dash versions.
