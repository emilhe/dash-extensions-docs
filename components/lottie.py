from dash_extensions.enrich import Dash, html
from dash_extensions import Lottie

url = "https://assets9.lottiefiles.com/packages/lf20_YXD37q.json"
app = Dash(__name__)
app.layout = Lottie(options=dict(
    loop=True, autoplay=True,
    rendererSettings=dict(preserveAspectRatio='xMidYMid slice')
), width="35%", height="35%", url=url)

if __name__ == '__main__':
    app.run_server()