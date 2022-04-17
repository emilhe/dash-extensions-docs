from dash_extensions.enrich import DashProxy, Input, html, NoOutputTransform

app = DashProxy(transforms=[NoOutputTransform()])
app.layout = html.Div([html.Button("Click me", id="btn")])
# Clientside callback.
f = "function(n_clicks){console.log('Hello world! Click count = ' + n_clicks);}"
app.clientside_callback(f, Input("btn", "n_clicks"))  # no Output is OK

@app.callback(Input("btn", "n_clicks"))  # no Output is OK
def func(n_clicks):
    print(f"Click count = {n_clicks}")

if __name__ == "__main__":
    app.run_server()