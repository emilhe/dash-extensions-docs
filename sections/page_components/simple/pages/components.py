import plotly.express as px
from dash import dcc

NAVBAR_ID = "navbar"

df = px.data.iris()
# Sunburst graph.
fig = px.sunburst(df, path=['species', 'sepal_width', 'sepal_length'])
sunburst_graph = dcc.Graph(figure=fig)
# Bar graph.
fig = px.bar(df, x="sepal_width", y="sepal_length")
bar_graph = dcc.Graph(figure=fig)
