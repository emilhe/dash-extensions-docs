from dash_extensions.enrich import DashProxy
from dash_extensions import Mermaid

app = DashProxy()
app.layout = Mermaid(chart="""
graph TD;
A-->B;
A-->C;
B-->D;
C-->D;
""")

if __name__ == "__main__":
    app.run_server()