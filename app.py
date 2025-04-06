import os

import dash_mantine_components as dmc
from dash_extensions.enrich import DashProxy, page_registry
from dash_extensions.snippets import fix_page_load_anchor_issue

from utils.markdown import register_pages
from utils.routes import register_routes
from utils.ui import create_app_shell

stylesheets = [
    dmc.styles.CODE_HIGHLIGHT,
    dmc.styles.NOTIFICATIONS,
]

# Add Google Analytics. # TODO: Does this work? TEST IT (!)
gtag = os.getenv("gtag", "")
scripts = [
    f"https://www.googletagmanager.com/gtag/js?id={gtag}",
]
# Setup app.
app = DashProxy(
    __name__,
    use_pages=True,
    update_title=None,
    suppress_callback_exceptions=True,
    external_stylesheets=stylesheets,
    external_scripts=scripts,
)
# Register component blueprints.
register_pages(app, "sections", order=0)
register_pages(app, "transforms", order=10)
register_pages(app, "components", order=20)
# Bind layout.
app.layout = create_app_shell(page_registry.values(), fix_page_load_anchor_issue(app, 500))


# Make server available for gunicorn.
server = app.server
register_routes(server)


if __name__ == "__main__":
    app.run(port=7879, debug=True)
