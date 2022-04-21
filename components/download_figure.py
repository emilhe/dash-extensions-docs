import plotly.graph_objects as go
from dash_extensions.enrich import DashProxy, html, Output, Input, dcc

app = DashProxy()
app.layout = html.Div([html.Button("Download", id="btn_fig"), dcc.Download(id="download_fig")])

@app.callback(Output("download_fig", "data"), [Input("btn_fig", "n_clicks")], prevent_initial_call=True)
def download(n_clicks):
    f = go.Figure()
    return dcc.send_bytes(f.write_image, "figure.png")  # requires the kaleido package

if __name__ == '__main__':
    app.run_server()