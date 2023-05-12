from dash_extensions.enrich import DashProxy, page_registry
from dash_extensions.snippets import fix_page_load_anchor_issue
from utils.markdown import register_pages
from utils.ui import create_app_shell

app = DashProxy(__name__, use_pages=True, update_title=None, suppress_callback_exceptions=True)
# Register component blueprints.
register_pages(app, "getting_started", order=0)
register_pages(app, "transforms", order=10)
register_pages(app, "components", order=20)
# Bind layout.
app.layout = create_app_shell(page_registry.values(), fix_page_load_anchor_issue(app, 500))
# Make server available for gunicorn.
server = app.server

if __name__ == '__main__':
    app.run_server(port=7879)
