import time
import plotly.express as px
from dash_extensions.enrich import DashProxy, Output, Input, State, ServersideOutput, html, dcc, \
    ServersideOutputTransform

app = DashProxy(transforms=[ServersideOutputTransform()])
app.layout = html.Div(
    [
        html.Button("Query data", id="btn"),
        dcc.Dropdown(id="dd"),
        dcc.Graph(id="graph"),
        dcc.Loading(dcc.Store(id="store"), fullscreen=True, type="dot"),
    ]
)

@app.callback(ServersideOutput("store", "data"), Input("btn", "n_clicks"), prevent_initial_call=True)
def query_data(n_clicks):
    time.sleep(3)  # emulate slow database operation
    return px.data.gapminder()  # no JSON serialization here

@app.callback(Output("dd", "options"),  Output("dd", "value"), Input("store", "data"), prevent_initial_call=True)
def update_dd(df):
    options = [{"label": column, "value": column} for column in df["year"]]   # no JSON de-serialization here
    return options, options[0]['value']

@app.callback(Output("graph", "figure"), [Input("dd", "value"), State("store", "data")], prevent_initial_call=True)
def update_graph(value, df):
    df = df.query("year == {}".format(value))  # no JSON de-serialization here
    return px.sunburst(df, path=["continent", "country"], values="pop", color="lifeExp", hover_data=["iso_alpha"])

if __name__ == "__main__":
    app.run_server()