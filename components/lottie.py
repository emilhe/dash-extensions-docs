from dash_extensions.enrich import DashProxy
from dash_extensions import Lottie

app = DashProxy()
app.layout = Lottie(
    options=dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice')),
    width="256px", url="https://assets9.lottiefiles.com/packages/lf20_YXD37q.json"
)

if __name__ == '__main__':
    app.run_server()