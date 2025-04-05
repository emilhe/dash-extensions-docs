import json

from dash_extensions.enrich import DashProxy, Input, Output, html
from dash_extensions.events import SimpleEvent, resolve_event_components

app = DashProxy()


class SomeEvent(SimpleEvent):
    message: str
    number: int


@app.callback(Input("btn", "n_clicks"))
def fire_event(n_clicks):
    if n_clicks is not None:
        SomeEvent(message="Hello world!", number=42).dispatch()


@app.callback(
    Output("log", "children"),
    SomeEvent.add_listener(),
    prevent_initial_call=True,
)
def process_event(event: dict):
    return json.dumps(event)


app.layout = html.Div(
    [
        html.Button("Click me!", id="btn"),
        html.Div(id="log"),
    ]
    + resolve_event_components()  # must be called *after* all callbacks have been defined
)


if __name__ == "__main__":
    app.run()
