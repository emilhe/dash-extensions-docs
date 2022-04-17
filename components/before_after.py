from dash_extensions.enrich import DashProxy, html
from dash_extensions import BeforeAfter

app = DashProxy()
app.layout = html.Div([
    BeforeAfter(before="/assets/lena_bw.png", after="/assets/lena_color.png", width=256, height=256)
])

if __name__ == "__main__":
    app.run_server()