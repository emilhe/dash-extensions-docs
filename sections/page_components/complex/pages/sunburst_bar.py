import plotly.express as px
from dash import html, register_page, dcc
from pages.components import sunburst_graph, bar_graph, df

register_page(
    __name__,
    path='/bar',
    page_components=[sunburst_graph, bar_graph],
    # Place the graphs on each side of the page main page content (a scatter plot).
    page_properties={
        sunburst_graph: {"style": {"grid-column": "1", "grid-row": "2"}},
        bar_graph: {"style": {"grid-column": "3", "grid-row": "2"}},
        "links": {"style": {"grid-column": "1 / span 3", "grid-row": "3"}}
    },
)

layout = html.Div([
    # Header, placed in row 1, above everything else.
    html.H2("Sunburst and Bar", style= {"grid-column": "1 / span 3"}), 
    # Other page content (here, a scatter plot), placed in row 2, between the graphs.
    dcc.Graph(
        figure=px.scatter(df, x="sepal_width", y="sepal_length"), 
        style={"grid-column": "2", "grid-row": "2"}
    )
], style={"display": "contents"})
