import plotly.express as px
from dash import html, register_page, dcc
from pages.components import sunburst_graph, bar_graph, df, NAVBAR_ID

register_page(
    __name__,
    path='/scatter_bar',
    page_components=[sunburst_graph, bar_graph],
    page_properties={
        # Place the graphs in row 2, below the header, on each side of the page layout.
        sunburst_graph: {"style": {"grid-column": "1", "grid-row": "2"}},
        bar_graph: {"style": {"grid-column": "3", "grid-row": "2"}},
        # Place links in row 3, below everything else.
        NAVBAR_ID: {"style": {"grid-column": "1 / span 3", "grid-row": "3"}}
    },
)

page_header = html.H2("Sunburst, Scatter and Bar")
page_content = dcc.Graph(
    figure=px.scatter(df, x="sepal_width", y="sepal_length", color_discrete_sequence=[px.colors.qualitative.Plotly[1]]), 
)
layout = html.Div([
    # Place the header in row 1, above everything else.
    html.Div(page_header, style= {"grid-column": "1 / span 3"}),
    # Put other page content in row 2, between the graphs.
    html.Div(page_content, style= {"grid-column": "2", "grid-row": "2"}),
], style={"display": "contents"})
