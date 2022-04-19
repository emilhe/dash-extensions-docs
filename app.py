import dash_labs as dl

from dash_down.directives import DashProxyDirective
from dash_extensions.enrich import DashProxy

from utils.markdown import register_folder, custom_code_renderer, PythonDirective
from utils.ui import app_shell

app = DashProxy(plugins=[dl.plugins.pages])
dpd = DashProxyDirective(custom_render=custom_code_renderer)
plugins = [dpd, PythonDirective()]
# Register component blueprints.
register_folder(app, "getting_started", plugins, order_map=dict(installation=0, javascript=1, enrich=2))
register_folder(app, "transforms", plugins, order=10)
register_folder(app, "components", plugins, order=20)
# Bind layout.
app.layout = app_shell(dl.plugins.page_container)

if __name__ == '__main__':
    app.run_server(port=7879)