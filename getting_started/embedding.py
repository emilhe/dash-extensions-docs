from dash_extensions.enrich import DashBlueprint, DashProxy, html, Output, Input

bp = DashBlueprint()
bp.layout = html.Div([html.Button('Click me!', id='btn'), html.Div(id='log')])

@bp.callback(Output('log', 'children'), Input('btn', 'n_clicks'))
def on_click(n_clicks):
    return f"Hello world {n_clicks}!"

app = DashProxy(prevent_initial_callbacks=True)  # could also be a normal Dash app
app.layout = html.Div([
    html.H2("Embedding"),  # main app layout
    bp.layout  # inject blueprint layout
])
bp.register_callbacks(app)  # bind callbacks to main app object

if __name__ == '__main__':
    app.run_server()