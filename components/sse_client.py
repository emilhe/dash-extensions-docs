from dash_extensions import SSE
from dash_extensions.enrich import DashProxy, Input, Output, html
from dash_extensions.streaming import sse_options
from sse_model import MyModel

API_ENDPOINT = "http://localhost:5000/steam"

# Create a small example app.
app = DashProxy(__name__)
app.layout = html.Div(
    [
        html.Button("Start streaming", id="btn"),
        SSE(id="sse", concat=True, animate_chunk=5, animate_delay=10),
        html.Div(id="response"),
    ]
)
# Render (concatenated, animated) text from the SSE component.
app.clientside_callback(
    "function(x){return x};",
    Output("response", "children"),
    Input("sse", "animation"),
)


@app.callback(
    Output("sse", "url"),
    Output("sse", "options"),
    Input("btn", "n_clicks"),
    prevent_initial_call=True,
)
def start_streaming(_):
    return API_ENDPOINT, sse_options(MyModel(content="Hello, world!"))


if __name__ == "__main__":
    app.run_server(port=7777)
