from dash_extensions.enrich import DashProxy, html, Input, NoOutputTransform

app = DashProxy(prevent_initial_callbacks=True, transforms=[NoOutputTransform()])
app.layout = html.Div([html.Button('Click me!', id='btn')])
app.clientside_callback("function(n_clicks){window.open('https://google.com');}", Input("btn", "n_clicks"))

if __name__ == '__main__':
    app.run_server()