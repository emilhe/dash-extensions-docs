import dash_mantine_components as dmc
from dash.exceptions import PreventUpdate
from dash import Dash, html, Output, Input

app = Dash()
app.layout = html.Div([
    dmc.NumberInput(id="celsius", label="Celsius"),
    dmc.NumberInput(id="fahrenheit", label="Fahrenheit"),
])

@app.callback(Output("celsius", "value"), Input("fahrenheit", "value"))
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
