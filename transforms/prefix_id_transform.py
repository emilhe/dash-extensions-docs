from dash_extensions.enrich import DashProxy, Input, Output, PrefixIdTransform, html

app = DashProxy(transforms=[PrefixIdTransform(prefix="some_prefix")])
app.layout = html.Div([html.Button("Click me", id="btn"), html.Div(id="log")])


@app.callback(Output("log", "children"), Input("btn", "id"))
def func(btn_id):  # argument is omitted from the function
    return f"The button id is {btn_id}"


if __name__ == "__main__":
    app.run()
