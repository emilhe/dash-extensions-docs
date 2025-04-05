from dash_extensions.enrich import DashProxy, Input, Output, html
from dash_extensions.events import add_event_listener, dispatch_event, resolve_event_components

app = DashProxy()


@app.callback(Input("btn_simple", "n_clicks"))
def fire_event(n_clicks):
    if n_clicks is not None:
        print("Firing event")
        dispatch_event("some-event")


@app.callback(Output("log_simple", "children"), add_event_listener("some-event"), prevent_initial_call=True)
def process_event(_):
    print("Processing event")
    return "Event received!"


app.layout = html.Div(
    [
        html.Button("Click me!", id="btn_simple"),
        html.Div(id="log_simple"),
    ]
    + resolve_event_components()  # must be called *after* all callbacks have been defined
)


if __name__ == "__main__":
    app.run()
