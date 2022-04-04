from dash_extensions.enrich import DashProxy, html, Input, Output, State
from dash_extensions import EventListener

# JavaScript event(s) that we want to listen to and what properties to collect.
event = {"event": "click", "props": ["srcElement.className", "srcElement.innerText"]}
# Create small example app
app = DashProxy(prevent_initial_callbacks=True)
app.layout = html.Div([
    EventListener(
        html.Div("Click here!", className="stuff"),
        events=[event], logging=True, id="el"
    ),
    html.Div(id="log")
])

@app.callback(Output("log", "children"), Input("el", "n_events"), State("el", "event"))
def click_event(n_events, e):
    return ",".join(f"{prop} is '{e[prop]}' " for prop in event["props"]) + f" (number of clicks is {n_events})"

if __name__ == "__main__":
    app.run_server()
