import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Output, Input, html, DashProxy, LogTransform, DashLogger

app = DashProxy(transforms=[LogTransform()])
app.layout = html.Div([dmc.Button("Run", id="btn"), dmc.Text(id="txt")])

@app.callback(Output("txt", "children"), Input("btn", "n_clicks"), log=True)
def do_stuff(n_clicks, logger: DashLogger):
    if not n_clicks:
        raise PreventUpdate()
    logger.info("Here goes some info")
    logger.warning("This is a warning")
    logger.error("Some error occurred")
    return f"Run number {n_clicks} completed"

if __name__ == '__main__':
    app.run_server()