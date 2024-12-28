from dash_extensions import SSE
from dash_extensions.enrich import DashProxy, Input, Output, html
from dash_extensions.streaming import sse_options
from sse_model import MyModel

API_ENDPOINT = "http://localhost:5000/sse"

# Create a small example app.
app = DashProxy(__name__)
app.layout = html.Div(
    [
        html.Button("Click me", id="btn"),
        SSE(id="sse"),
        html.Div(id="sse-value"),
    ]
)
# Update the output with the value of the SSE stream.
app.clientside_callback("(x) => console.log(x)", Output("sse-value", "children"), Input("sse", "value"))


@app.callback(Output("sse", "url"), Output("sse", "options"), Input("btn", "n_clicks"), prevent_initial_call=True)
def start_streaming(_):
    return API_ENDPOINT, sse_options(MyModel(content="Hello, world!"))


if __name__ == "__main__":
    app.run_server(port=7777)
