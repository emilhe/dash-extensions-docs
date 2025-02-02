from dash_extensions.enrich import DashProxy, Input, Output, html
from dash_extensions.logging import DivLogHandler

log_handler = DivLogHandler()
logger = log_handler.setup_logger(__name__)

app = DashProxy()
app.layout = html.Div(
    [btn := html.Button("Run", id="div_run"), txt := html.Div(id="div_txt")]
    + log_handler.embed()
)


@app.callback(
    Output(txt, "children"), Input(btn, "n_clicks"), prevent_initial_call=True
)
def do_stuff(n_clicks):
    logger.info("Here goes some info")
    logger.warning("This is a warning")
    logger.error("Some error occurred")
    return f"Run number {n_clicks} completed"


if __name__ == "__main__":
    app.run()
