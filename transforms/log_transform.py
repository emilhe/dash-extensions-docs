from dash.exceptions import PreventUpdate
from dash_extensions.enrich import (
    DashLogger,
    DashProxy,
    Input,
    LogTransform,
    Output,
    html,
)

app = DashProxy(transforms=[LogTransform()])
app.layout = html.Div([html.Button("Run", id="btn"), html.Div(id="txt")])


@app.callback(Output("txt", "children"), Input("btn", "n_clicks"), log=True)
def do_stuff(n_clicks, dash_logger: DashLogger):
    if not n_clicks:
        raise PreventUpdate()
    dash_logger.info("Here goes some info")
    dash_logger.warning("This is a warning")
    dash_logger.error("Some error occurred")
    return f"Run number {n_clicks} completed"


if __name__ == "__main__":
    app.run(debug=True)
