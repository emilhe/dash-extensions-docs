from dash_extensions import BeforeAfter
from dash_extensions.enrich import DashProxy, html

app = DashProxy()
app.layout = html.Div(
    [
        BeforeAfter(
            before=dict(src="/assets/lena_bw.png"),
            after=dict(src="/assets/lena_color.png"),
            width="256",
            height="256",
        )
    ]
)

if __name__ == "__main__":
    app.run()
