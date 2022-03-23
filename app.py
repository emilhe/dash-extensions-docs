import dash_labs as dl

from dash import Output, Input, Dash
from dash_extensions.enrich import register

from dash_down.express import md_to_blueprint_dmc
from lib.appshell import AppShell

app = Dash(plugins=[dl.plugins.pages])

# TODO: Testing blueprints
blueprint = md_to_blueprint_dmc("components/before_after.md")
register(blueprint, "components.before_after")

app.layout = AppShell(dl.plugins.page_container)
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


if __name__ == '__main__':
    app.run_server()
