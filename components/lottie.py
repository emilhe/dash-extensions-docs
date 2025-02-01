from dash_extensions import Lottie
from dash_extensions.enrich import DashProxy

app = DashProxy()
app.layout = Lottie(
    options=dict(
        loop=True,
        autoplay=True,
        rendererSettings=dict(preserveAspectRatio="xMidYMid slice"),
    ),
    width="50%",
    url="https://assets8.lottiefiles.com/packages/lf20_bkwin39r.json",
)

if __name__ == "__main__":
    app.run()
