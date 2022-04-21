import dash_labs as dl
from dash_extensions.enrich import DashProxy, PrefixIdTransform
from utils.markdown import register_pages
from utils.ui import app_shell

app = DashProxy(plugins=[dl.plugins.pages])
# Register component blueprints.
register_pages(app, "getting_started", order_map=dict(installation=0, javascript=1, enrich=2))
register_pages(app, "transforms", order=10)
register_pages(app, "components", order=20)
# Bind layout.
app.layout = app_shell(dl.plugins.page_container)

if __name__ == '__main__':
    app.run_server(port=7879)
