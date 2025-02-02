import dash_mantine_components as dmc
from dash_extensions.enrich import DashProxy, Input, Output, html
from dash_extensions.logging import NotificationsLogHandler

log_handler = NotificationsLogHandler()
logger = log_handler.setup_logger(__name__)

app = DashProxy(external_stylesheets=[dmc.styles.NOTIFICATIONS])
app.layout = dmc.MantineProvider(
    [btn := html.Button("Run", id="dmc_run"), txt := html.Div(id="dmc_txt")]
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
