import plotly.express as px
from dash import dcc, dash_table

# Table.
df = px.data.iris()
table = dash_table.DataTable(df.to_dict('records')[:5], [{"name": i, "id": i} for i in df.columns])
# Scatter graph.
fig = px.scatter(df, x="sepal_width", y="sepal_length")
scatter_graph = dcc.Graph(figure=fig)
# Bar graph.
fig = px.bar(df, x="sepal_width", y="sepal_length")
bar_graph = dcc.Graph(figure=fig)
