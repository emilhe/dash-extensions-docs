### DeferScript

The `DeferScript` component makes it possible to _defer_ the loading of javascript code until after the DOM is loaded, which is needed e.g. for rendering dynamic content. Examples include [table sorting](https://stackoverflow.com/questions/10683712/html-table-sort/55730907#55730907) and drawing libraries such as is [draw.io](https://app.diagrams.net/). Here is an example of the latter,

.. dash-proxy:: components.defer_script

.. api-doc:: dash_extensions.DeferScript