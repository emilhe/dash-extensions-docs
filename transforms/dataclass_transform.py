from datetime import datetime
from dataclasses import dataclass
from dash_extensions.enrich import DashProxy, Input, html, DataclassTransform, dcc, Output, State

@dataclass
class Person:
    name: str
    date_of_birth: datetime

app = DashProxy(transforms=[DataclassTransform()])
app.layout = html.Div([
    dcc.Input(id="name", value="John Doe"),
    dcc.DatePickerSingle(id="picker", date=datetime(1990, 1, 1)),
    dcc.Store(id="store"),
    html.Button("Submit", id="btn"),
    html.Div(id="log")
])

@app.callback(
    Input("btn", "n_clicks"),
    State("name", "value"),
    State("picker", "date"),
    Output("store", "data")
)
def submit(_, name, date):
    dt = datetime.fromisoformat(date)
    return Person(name, dt)  # no (manual) serialization here

@app.callback(
    Output("log", "children"),
    Input("store", "data"),
)
def log(person: Person):
    return f"{person.name} was born on {person.date_of_birth}"  # no (manual) deserialization here

if __name__ == "__main__":
    app.run_server()
