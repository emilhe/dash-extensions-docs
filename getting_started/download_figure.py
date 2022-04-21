import plotly.graph_objects as go
from dash import Dash, html, Output, Input, dcc

app = Dash()
app.layout = html.Div([html.Button("Download", id="btn"), dcc.Download(id="download")])

@app.callback(Output("download", "data"), [Input("btn", "n_clicks")])
def download(n_clicks):
    f = go.Figure()
    return dcc.send_bytes(f.write_image, "figure.png")  # requires the kaleido package

if __name__ == '__main__':
    app.run_server()