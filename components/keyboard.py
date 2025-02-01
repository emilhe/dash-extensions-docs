import json

from dash_extensions import Keyboard
from dash_extensions.enrich import DashProxy, Input, Output, State, dcc, html

# Create small example app
app = DashProxy()
app.layout = html.Div(
    [
        Keyboard(
            dcc.Input(
                placeholder="If you enter [a, b, c] or hit [Enter], the callback will fire.",
                id="message",
                style=dict(width="100%"),
            ),
            captureKeys=["Enter", "a", "b", "c"],
            id="keyboard",
        ),
        html.Div(id="log"),
    ]
)


@app.callback(
    Output("log", "children"),
    Input("keyboard", "n_keydowns"),
    State("keyboard", "keydown"),
)
def track_keydown(_, event):
    return json.dumps(event)


if __name__ == "__main__":
    app.run()
