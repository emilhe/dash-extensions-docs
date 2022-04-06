from dash_extensions import EventSource
from dash_extensions.enrich import html, dcc, Output, Input, DashProxy

# Client-side function (for performance) that updates the graph.
update_graph = """function(msg) {
    if(!msg){return {};}  // no data, just return
    const data = JSON.parse(msg);  // read the data
    return {data: [{y: data, type: "scatter"}]}};  // plot the data
"""
# Create small example app.
app = DashProxy(__name__)
app.layout = html.Div([
    EventSource(id="sse", url="http://127.0.0.1:5000/random_data"),
    dcc.Graph(id="graph")
])
app.clientside_callback(update_graph, Output("graph", "figure"), Input("sse", "message"))

if __name__ == "__main__":
    app.run_server(port=9898)