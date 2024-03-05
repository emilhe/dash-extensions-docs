from dash import html, register_page, page_container
from pages.components import table, scatter_graph

register_page(
    __name__,
    path='/scatter',
    page_components=[table, scatter_graph],
    page_properties={
        table: {'style_table': {'color': 'blue'}},
    }
)

layout = html.H2("Scatter")
