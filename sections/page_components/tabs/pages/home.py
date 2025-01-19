import dash
from dash import html, dcc

tab = dcc.Tab(label='Home', value='tab-0', children=["Home"])

dash.register_page(__name__, path="/", page_properties={"tabs": {"value": "tab-0"}}, page_components=[tab])

layout = html.Div()