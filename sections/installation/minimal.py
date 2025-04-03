from dash_extensions import Lottie
from dash_extensions.enrich import DashProxy

app = DashProxy()
app.layout = Lottie(
    options=dict(
        loop=True,
        autoplay=True,
        style=dict(width="25%", margin="auto"),
    ),
    url="https://assets6.lottiefiles.com/packages/lf20_rwwvwgka.json",
)

if __name__ == "__main__":
    app.run()
