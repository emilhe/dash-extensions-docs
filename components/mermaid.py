from dash_extensions import Mermaid
from dash_extensions.enrich import DashProxy

app = DashProxy()
app.layout = Mermaid(
    chart="""
graph TD;
A-->B;
A-->C;
B-->D;
C-->D;
""",
    # It is recommended to a an id, otherwise you may see 'querySelector' errors
    id="mermaid-chart",
)

if __name__ == "__main__":
    app.run()
