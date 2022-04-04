from dash_extensions.enrich import DashProxy
from dash_extensions import Purify

app = DashProxy()
app.layout = Purify("This is <b>html</b>")

if __name__ == "__main__":
    app.run_server()