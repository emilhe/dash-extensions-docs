from dash import html, register_page
from pages.components import sunburst_graph, bar_graph

register_page(
    __name__,
    path='/bar',
    page_components=[sunburst_graph, bar_graph],
)

layout = html.H2("Sunburst and Bar")
