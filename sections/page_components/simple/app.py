from dash_extensions.pages import setup_page_components
from dash import Dash, html, page_container, dcc, page_registry
from pages.components import NAVBAR_ID

app = Dash(__name__, use_pages=True)
links = [html.Div(dcc.Link(p["name"], href=p["path"])) for p in page_registry.values()]
app.layout = html.Div([
    page_container,  # page layout is rendered here
    setup_page_components(),  # page components are rendered here
    html.Div(links, id=NAVBAR_ID),  # simple navigation bar
])

if __name__ == "__main__":
    app.run_server(port=7777)
