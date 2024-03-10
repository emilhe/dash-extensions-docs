## Pages

The `pages` module extends [Dash Pages](https://dash.plotly.com/urls), a framework for making multi-page apps in Dash. It introduces the concept of _page components_ (previously known as dynamic components), which are components that are only visible on particular pages, and _page properties_, which are component property definitions that apply only to specific pages.

### Why not just use Dash Pages?

Let's start with a bit of background of the inner workings of Dash Pages. Each time the url changes, Dash Pages renders the layout of the (new) page into a container (`dash.page_container`), purging the layout of the previous page from the [DOM](https://www.w3schools.com/whatis/whatis_htmldom.asp) in the process. A key advantage is approach is _scalability_. Adding more pages doesn't impact performance. However, it also comes with a number of disadvantages

* Components can't be shared between pages. You can of course share component definitions in terms of code, but the component itself is re-created each time the user navigates to a new page. Hence, you'll need to do any state synchronization yourself
* As the previous page layout is purged from the DOM, the (page) layout has to be rendered from scratch every time the user navigates to a page. If the rendering is expensive, this can become a (significant) issue, if the user navigates a lot between pages
* As the layout rendering happens in Python, navigation requires interaction with the server (which is inherently slow)

In contrast to the layout of Dash Pages, page components are never purged from the DOM. Instead, their visibility is toggled as the url changes. This design offers a number of advantages,

* Components can be shared between pages, thereby eliminating the need for manual state synchronization
* As page components are never purged from the DOM, subsequent renders will be rapid. If the rendering is expensive, and the user navigates a lot between pages, the performance difference versus the "normal" Dash Pages approach can be like night and day
* As navigation is simply a matter of toggling element visibility, interaction with the server (which is inherently slow) is not necessary

The main drawback of page components is that performance may degrade as you add more page component since they are never purged from the DOM. This issue can be mitigated by cleaning up the layout of large/expensive components manually (i.e. using callbacks). However, doing so deteriorates the advantages in the process, and adds complexity to the app. Hence, it is not recommended to go down this path, unless performance issues are observed.

### Page components

As a simple example, let's consider an app that has two pages. Both pages share the same sunburst chart, but the second page adds a bar chart next to it. The `app.py` file will look similar to a normal Dash Pages app,

.. python-code:: sections.page_components.simple.app

apart from the `setup_page_components()` call. This function performs all the magic, and returns the container into which page component are rendered. To enable referencing the graphs components from the pages, they are defined in a separate `components.py` file,

.. python-code:: sections.page_components.simple.pages.components

Page component are assigned to a page by passing them via the `page_components` keyword argument of the `register_page` function. The first page is,

.. python-code:: sections.page_components.simple.pages.sunburst

and the second page is almost identical,

.. python-code:: sections.page_components.simple.pages.sunburst_bar

Notice that the bar graph was added as page components in this example. Since its not shared, it could also have been included as part of the page layout. Here is the application in action,

![Component sharing](/assets/page_components_simple.gif)

### Page properties

When components are shared between pages, a need for page-specific adjustments tends to arise. As a simple example, say that we want the graphs to be side-by-side on the second page, while on other pages (i.e. page one) the layout should remain unchanged. This behavior can be achived by passing the appropriate styles via the `page_properties` argument of the `register_page` function,

```python
from dash import html, register_page
from pages.components import sunburst_graph, bar_graph

register_page(
    __name__,
    path='/bar',
    page_components=[sunburst_graph, bar_graph],
    page_properties={
        sunburst_graph: {'style': {'width': '50%', 'float': 'left'}},
        bar_graph: {'style': {'width': '50%', 'float': 'left'}},
    }
)

layout = html.H2("Sunburst and Bar")
```

When the user navigates to the scatter page, the properties are applied automatically. Simiarly, when the user navigates to another page, the properties are reverted to their original values.

![Page properties](/assets/page_properties_simple.gif)

### The best of both worlds

With page components offering distinct advantages and disadvantages compared to page layouts, some scenarios are best addressed through a hybrid approach. Achiving the desired page structure can seem a bit more challenging, as page component are assigned to the layout on app initialization, while page layouts are added dynamically. One way to address this heterogeneity to use [CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) to control the main page structure, flow all elements (that needs to be positioned in this grid) to the main container using [CSS display:contents](https://caniuse.com/css-display-contents), and position the elements dynamically via page properties. 

To demonstrate this approach, we'll consider a simple example, building on the code from the previous section. Specifically, we'll be adding some page content betweent the two graphs on page two. First, we modify `app.py` to use CSS grid for the main container,

.. python-code:: sections.page_components.complex.app

Note that the grid is initialized with 3 columns; that's because we need 3 columns to achieve the desired layout for page two. The grid layout should be chosen so as to accomodate the must granular strcture needed across all pages. To keep the layout of page one as before, we must add CSS to specify that the graph should span all 3 columns,

.. python-code:: sections.page_components.complex.sunburst

On page two, all three elements need a of bit of CSS to specify their respective positions,

.. python-code:: sections.page_components.complex.sunburst_bar

...





