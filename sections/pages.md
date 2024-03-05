## Pages

The `pages` module extends [Dash Pages](https://dash.plotly.com/urls), a framework for making multi-page apps in Dash. It introduces the concept of _page components_ (previously known as dynamic components), which are components that are only visible on particular pages, and _page properties_, which are component property definitions that apply only to specific pages.

### Dash pages

Before we dive into page components, a bit of background of the inner workings of Dash Pages comes in handy. Each time the url changes, Dash Pages renders the layout of the (new) page into a particular container (`dash.page_container`), purging the layout of the previous page from the [DOM](https://www.w3schools.com/whatis/whatis_htmldom.asp) in the process. A key advantage is approach is _scalability_. Adding more pages doesn't impact performance. However, it also comes with a number of disadvantages

* Components cannot be (truly) shared between pages. You can of course share component definitions in terms of code, but the component itself is re-created each time the user navigates to a new page. Hence, you'll need to do any state synchronization yourself
* As the previous page layout is purged from the DOM, the (page) layout has to be rendered from scratch every time the user navigates to a page. If the rendering is expensive, this can become a (significant) issue if the user navigates a lot between pages
* As the layout rendering happens in Python, navigation requires interaction with the server (which is inherently slow)

### Page components

In contrast to layout of Dash Pages, _page components_ are never purged from the DOM. Instead, their visibility is toggled as the url changes. Page components offer a number of advantages as compared to the "normal" Dash Pages approach,

* Components can be (truly) shared between pages, which improves performance, and eliminates the need for manual state synchronization
* As page components are never purged from the DOM, subsequent renders will be rapid. If the rendering is expensive, and the user navigates a lot between pages, the performance difference versus the "normal" Dash Pages approach can be like night and day
* As navigation is simply a matter of toggling element visibility, interaction with the server (which is inherently slow) is not necessary

The main drawback of page components is that performance may degrade as you add more page component since they are never purged from the DOM. This issue can be mitigated by cleaning up the layout of large/expensive components manually (i.e. using callbacks), but doing so deteriorates the advantages in the process, and adds complexity to the app. Hence, it is not recommended to go down this path, unless performance issues are observed.

### Component sharing

As a simple example, let's consider an app that has two pages. Both pages share the same table, but while the first page shows a scatter plot, the second page show a bar chart. The `app.py` file will look similar to a normal Dash Pages app,

.. python-code:: sections.page_components.simple.app

apart from the `setup_page_components()` call. This function performs all the magic, and returns the container into which page component are rendered. To enable referencing the table and graphs component from the pages, they are defined in a separate `components.py` file,

.. python-code:: sections.page_components.simple.pages.components

Page component are assigned to a page by passing them via the `page_components` of the `register_page` function. Hence, the first page is simply,

.. python-code:: sections.page_components.simple.pages.scatter

and the second page is almost identical,

.. python-code:: sections.page_components.simple.pages.bar

Notice that the graphs are added as page components in this example. Since they are not shared, they could also have been included as part of the page layout. To complete the app, a simple landing page is added,

.. python-code:: sections.page_components.simple.pages.home

Here is the application in action,

![Component sharing](/assets/page_components_simple.gif)

Notice how the table selection is persisted across pages. This is the kind of behavior that would be hard to achieve without page components. 

### Page properties

When components are shared between pages, a need for page-specific adjustments tends to arise. As a simple example, say that we want the table font to be blue on the scatter page, but not on other pages. This behavior can be achived using _page properties_ by passing the appropriate styles via the `page_properties` argument of the `register_page` function.

```python
from dash import html, register_page, page_container
from pages.components import table, scatter_graph

register_page(
    __name__,
    path='/scatter',
    page_components=[table, scatter_graph],
    page_properties={table: {'style_table': {'color': 'blue'}}}
)
```

When the user navigates to the scatter page, the properties are applied automatically. Simiarly, when the user navigates to another page, the properties are reverted to their original values.

![Page properties](/assets/page_properties_simple.gif)

Notice how the style changes between pages, while the table selection remains persistant.

### The best of both worlds







