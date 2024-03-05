from dash import html, register_page
from pages.components import table, bar_graph

register_page(
    __name__,
    path='/bar',
    page_components=[table, bar_graph]
)

layout = html.H2("Bar")
