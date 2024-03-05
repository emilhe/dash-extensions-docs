from dash import Dash, html, Output, Input

app = Dash(prevent_initial_callbacks=True)
app.layout = html.Div([html.Button('Click me!', id='btn'), html.Div(id='dummy')])
app.clientside_callback("function(n_clicks){window.open('https://google.com');}",
                        Output("dummy", "children"), Input("btn", "n_clicks"))

if __name__ == '__main__':
    app.run_server()