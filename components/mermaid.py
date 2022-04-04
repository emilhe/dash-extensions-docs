from dash_extensions.enrich import DashProxy
from dash_extensions import Mermaid

chart = """
graph TD;
A-->B;
A-->C;
B-->D;
C-->D;
"""
app = DashProxy()
app.layout = Mermaid(chart=chart)

if __name__ == "__main__":
    app.run_server()
