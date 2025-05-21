## Javascript

In Dash, component properties must be JSON serializable. However, many React components take JavaScript functions (or objects) as inputs, which can make it tedious to write Dash wrappers. To ease the process, `dash-extensions` implements a simple bridge for passing function handles (and other variables) as component properties. The `javascript` module is the Python side of the bridge, while the `dash-extensions-js` package [on npm](https://www.npmjs.com/package/dash-extensions-js) forms the JavaScript side. 

In the examples below, we will consider the `GeoJSON` component in `dash-leaflet==0.1.10`. The complete example apps are available in the [dash-leaflet documentation](https://www.dash-leaflet.com/docs/geojson_tutorial).

### JavaScript variables

Any JavaScript variable defined in the (global) window object can passed as a component property. Hence, if we create a .js file in the assets folder with the following content,

```js
window.myNamespace = Object.assign({}, window.myNamespace, {  
    mySubNamespace: {  
        pointToLayer: function(feature, latlng, context) {  
            return L.circleMarker(latlng)  
        }  
    }  
});
```

the `pointToLayer` function of the `myNamespace.mySubNamespace` namespace can now be used as a component property,

```python
import dash_leaflet as dl
from dash_extensions.javascript import Namespace
...
ns = Namespace("myNamespace", "mySubNamespace")
geojson = dl.GeoJSON(data=data, options=dict(pointToLayer=ns("pointToLayer")))
```

Note that this approach is not limited to function handles, but can be applied for any data type.

### Inline JavaScript

The `assign` function of the `javascript` module provides a more compact syntax where the JavaScript code is written as a string directly in the Python file. The previous example is thus reduced to,

```python
import dash_leaflet as dl
from dash_extensions.javascript import assign
...
point_to_layer = assign("function(feature, latlng, context) {return L.circleMarker(latlng);}")
geojson = dl.GeoJSON(data=data, options=dict(pointToLayer=point_to_layer))
```

without the need for creating any .js files manually. The syntax is particularly well suited for small JavaScript code snippets and/or examples. Note that under the hood, the inline functions are transpiled into a .js file, which is written to the assets folder.

### Arrow functions

In some cases, it might be sufficient to wrap an object as an arrow function, i.e. a function that just returns the (constant) object. This behaviour can be achieved with the following syntax,

```python
import dash_leaflet as dl
from dash_extensions.javascript import arrow_function
...
geojson = dl.GeoJSON(hoverStyle=arrow_function(dict(weight=5, color='#666', dashArray='')), ...)
```