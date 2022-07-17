from dash.exceptions import PreventUpdate
from dash_extensions.enrich import DashProxy, html, Input, Operator, OperatorTransform, OperatorOutput, dcc, Output

app = DashProxy(transforms=[OperatorTransform()])
app.layout = html.Div([
    html.Button("Append and sort", id="btn"),
    dcc.Store(id="numbers", data=[1, 2, 3, 4, 5]),
    html.Div(id="json")
])
app.clientside_callback("function(x){return JSON.stringify(x);}",
                        Output("json", "children"), Input("numbers", "data"))

@app.callback(OperatorOutput("numbers", "data"), Input("btn", "n_clicks"))
def action(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    operator = Operator()
    operator.list.append(n_clicks)
    operator.list.sort()
    return operator

if __name__ == '__main__':
    app.run_server()
