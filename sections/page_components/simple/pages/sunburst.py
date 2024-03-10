from dash import html, register_page
from pages.components import sunburst_graph

register_page(
    __name__,
    path='/',
    page_components=[sunburst_graph],
)

layout = html.H2("Sunburst")
