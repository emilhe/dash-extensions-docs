from dash import html, register_page
from pages.components import sunburst_graph

register_page(
    __name__,
    path='/',
    page_components=[sunburst_graph],
    page_properties={sunburst_graph: {"style": {"grid-column": "1 / span 3"}}},
)

layout = html.H2("Sunburst")
