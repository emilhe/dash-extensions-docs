import dash_labs as dl
from dash_down import GITHUB_MARKDOWN_CSS_LIGHT
from dash_extensions.enrich import DashProxy, Output, Input
from dash_extensions.snippets import fix_page_load_anchor_issue
from utils.markdown import register_pages
from utils.ui import app_shell

app = DashProxy(__name__, plugins=[dl.plugins.pages], external_stylesheets=[GITHUB_MARKDOWN_CSS_LIGHT])
# Register component blueprints.
register_pages(app, "getting_started", order_map=dict(installation=0, javascript=1, enrich=2))
register_pages(app, "transforms", order=10)
register_pages(app, "components", order=20)
# Bind layout.
app.layout = app_shell([dl.plugins.page_container] + fix_page_load_anchor_issue(app, 250))
# Enable search bar.
app.clientside_callback(
    """
    function(value) {
        if (value) {
            document.getElementById(value).click()
        }
        return value
    }
    """,
    Output("dummy-container-for-header-select", "children"),
    Input("select-component", "value"),
)
# Make server available for gunicorn.
server = app.server

if __name__ == '__main__':
    app.run_server(port=7879)
