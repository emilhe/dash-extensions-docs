from dash import html, register_page
from pages.components import sunburst_graph, bar_graph

title = "Sunburst and Bar"
register_page(
    __name__,
    path=f'/bar',
    page_components=[sunburst_graph, bar_graph],
)

layout = html.H2(title)
