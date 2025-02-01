from dash.exceptions import PreventUpdate
from dash_extensions.enrich import DashProxy, Input, MultiplexerTransform, Output, html

app = DashProxy(transforms=[MultiplexerTransform()])
app.layout = html.Div(
    [
        html.Button("Left", id="left"),
        html.Button("Right", id="right"),
        html.Div(id="log"),
    ]
)


@app.callback(Output("log", "children"), Input("left", "n_clicks"))
def left(n_clicks):
    if not n_clicks:
        raise PreventUpdate()
    return "left"


@app.callback(Output("log", "children"), Input("right", "n_clicks"))
def right(n_clicks):
    if not n_clicks:
        raise PreventUpdate()
    return "right"


if __name__ == "__main__":
    app.run()
