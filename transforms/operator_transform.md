## OperatorTransform

Callbacks in Dash update component properties via _assignment_ operations. The `OperatorTransform` provides an api to perform a wider range of operations, including common `list` and `dict` operations, as well as (partial) updates of nested properties. To illustrate the concept, let's consider a small app that keeps a log of button click events. Since Dash callbacks do not support append operations natively, a commonly adopted strategy is to include the current value as `State`, perform the operation in the callback, and return the result, i.e.

.. python-code:: transforms.operator_log_original

While this approach _works_, there are two things that I don't love about it. First, I (and numerous other people, judging by forum posts) find the syntax a bit convoluted. The code required (adding an extra `State` object, an extra argument to the callback function, etc.) doesn't express the _intent_ (appending a log entry) clearly. Second, even though only a single element is added, **all elements are sent from the client to the server and back**. If the data is small (as in the example above, unless you do _a lot_ of clicks), it might not matter. But if the data is large (e.g. a big graph or table), this approach is horribly inefficient. Here is the same app using the `OperatorTransform`,

.. dash-proxy:: transforms.operator_log

Since the callback returns an _operation_, all element are _not_ exchanged between client and server. **Only the new element is sent from the server to the client**. Under the hood, a clientside callback is used to perform to append the log entry to the list. Hence, if the data is large, the `OperatorTransform` might enable (significant) performance improvements.

### Nested data structures

The `OperatorTransform` supports partial updates of nested properties. As an example, say we want to change the color of a trace in a graph. Common approaches include generating the figure from scratch, or passing the previous value via `State`. With the `OperatorTransform`, it is possible to change the color directly,

.. dash-proxy:: transforms.operator_scatter

### Chains of operations

In the previous example, only a single operation was performed. It is also possible to return a _chain_ of operations. Here is a small example, where a list is sorted after an element is appended,

.. dash-proxy:: transforms.operator_composite

### How does it work?

Under the hood, a client side callback performs the desired operation of the targeted component property. Hence, there is only a possible performance benefit for normal callbacks, not clientside callbacks.

### Benchmarks

Benchmarks will be added here. Stay tuned :)

