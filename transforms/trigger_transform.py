from dash_extensions.enrich import DashProxy, Output, Trigger, TriggerTransform, html

app = DashProxy(transforms=[TriggerTransform()])
app.layout = html.Div([html.Button("Click me", id="btn"), html.Div(id="log")])


@app.callback(
    Output("log", "children"), Trigger("btn", "n_clicks"), prevent_initial_call=True
)
def func():  # argument is omitted from the function
    return "You clicked the button"


if __name__ == "__main__":
    app.run()
