from dash_extensions.enrich import DashBlueprint, DashProxy, Input, Output, html

bp = DashBlueprint()
bp.layout = html.Div([html.Button("Click me!", id="btn"), html.Div(id="log")])


@bp.callback(Output("log", "children"), Input("btn", "n_clicks"))
def on_click(n_clicks):
    return f"Hello world {n_clicks}!"


if __name__ == "__main__":
    app = DashProxy(blueprint=bp)
    app.run()
