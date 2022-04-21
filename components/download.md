## Download

The `Download` component makes it possible for the user to download in-memory data and/or files. As per Dash 1.20.0, it has been [merged into `dash-core-components`](https://dash.plotly.com/dash-core-components/download). It was kept around in `dash-extensions` for some time to facilitate migration, but it has been dropped in `dash-extensions>=0.1.0`. 

### Send bytes

It is a [common misconception](https://stackoverflow.com/questions/62082946/dash-download-in-memory-generated-file-on-button-click-how-to-give-filename/62088521#62088521) that the `send_bytes` utility function takes an argument of type `bytes`. It does not, it takes a _function_ that writes to `BytesIO`. While this design choice might not seem obvious at first, it was made to improve compatibility with external libraries (`pandas`, `matplotlib`, etc.). 

To illustrate the syntax, let's look at a few examples. A typical use case for `send_bytes` is to write excel files,

.. python-code:: getting_started.download_excel

Another common use case is figure objects,

```python
import plotly.graph_objects as go
from dash import Dash, html, Input, Output
from dash_extensions import Download
from dash_extensions.snippets import send_bytes

app = Dash()
app.layout = html.Div([html.Button("Download", id="btn"), Download(id="download")])

@app.callback(Output("download", "data"), [Input("btn", "n_clicks")])
def download(n_clicks):
    f = go.Figure()
    return send_bytes(f.write_image, "figure.png")

if __name__ == '__main__':
    app.run_server()
```