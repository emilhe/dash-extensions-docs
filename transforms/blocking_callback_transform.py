import time
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import DashProxy, dcc, html, Output, Input, BlockingCallbackTransform

app = DashProxy(transforms=[BlockingCallbackTransform(timeout=10)])
app.layout = html.Div([html.Div(id="output"), dcc.Interval(id="trigger")])   # default interval is 1s

@app.callback(Output("output", "children"), Input("trigger", "n_intervals"), blocking=True)
def update(n_intervals):
    if not n_intervals:
        raise PreventUpdate()
    time.sleep(2)  # emulate slow database
    return f"Hello! (n_intervals is {n_intervals})"

if __name__ == '__main__':
    app.run_server()