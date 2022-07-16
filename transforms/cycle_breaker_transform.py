import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import DashProxy, html, Output, Input, CycleBreakerTransform, CycleBreakerInput

app = DashProxy(transforms=[CycleBreakerTransform()])
app.layout = html.Div([
    dmc.NumberInput(id="celsius", label="Celsius"),
    dmc.NumberInput(id="fahrenheit", label="Fahrenheit"),
])

@app.callback(Output("celsius", "value"), CycleBreakerInput("fahrenheit", "value"))
def update_celsius(value):
    if value is None:
        raise PreventUpdate()
    return (float(value) - 32) / 9 * 5

@app.callback(Output("fahrenheit", "value"), Input("celsius", "value"))
def update_fahrenheit(value):
    if value is None:
        raise PreventUpdate()
    return float(value) / 5 * 9 + 32

if __name__ == '__main__':
    app.run_server()
