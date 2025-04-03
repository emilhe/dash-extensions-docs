from dash_extensions import Purify
from dash_extensions.enrich import DashProxy

app = DashProxy()
app.layout = Purify(html="This is <b>html</b>")

if __name__ == "__main__":
    app.run()
