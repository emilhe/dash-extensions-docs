from dash_extensions.enrich import DashProxy, html
from dash_extensions import Ticker

app = DashProxy()
app.layout = Ticker("Some text", direction="toRight")

if __name__ == "__main__":
    app.run_server()