import dash_labs as dl
from dash_extensions.enrich import DashBlueprint, DashProxy, Input, Output, html


def page_name(i: int):
    return f"page{i}"


def make_page(i: int):
    page = DashBlueprint()
    page.layout = html.Div(
        [html.H2(f"Page {i}"), html.Button("Click me!", id="btn"), html.Div(id="log")]
    )

    @page.callback(Output("log", "children"), Input("btn", "n_clicks"))
    def on_click(n_clicks):
        return f"Hello world {n_clicks} from page {i}!"

    return page


app = DashProxy(prevent_initial_callbacks=True, plugins=[dl.plugins.pages])
# Register a few pages.
n_pages = 5
for i in range(n_pages):
    page = make_page(i)
    page.register(app, page_name(i), prefix=str(i))
# Setup main app layout.
app_shell = [html.H1("App shell"), dl.plugins.page_container]
navigation = html.Ul(
    [html.Li(html.A(page_name(i), href=page_name(i))) for i in range(n_pages)]
)
app.layout = html.Div(app_shell + [navigation], style=dict(display="block"))

if __name__ == "__main__":
    app.run()
