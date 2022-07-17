import datetime
import dash_mantine_components as dmc
from dash_extensions.enrich import DashProxy, html, Input, Operator, OperatorTransform, OperatorOutput

app = DashProxy(transforms=[OperatorTransform()])
app.layout = html.Div([
    html.Button("Click me", id="btn"),
    dmc.List(id="log", children=[]),
])

@app.callback(OperatorOutput("log", "children"), Input("btn", "n_clicks"))
def append_to_log(n_clicks):
    log_entry = f"{datetime.datetime.now().isoformat()}: BUTTON CLICKED (n_clicks={n_clicks})"
    return Operator().list.append(dmc.ListItem(log_entry))

if __name__ == '__main__':
    app.run_server()
