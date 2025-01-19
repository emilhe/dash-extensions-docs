from dash import dash, dcc
from dash_extensions.pages import setup_page_components, set_page_container_style_display_contents

app = dash.Dash(
    __name__, use_pages=True, suppress_callback_exceptions=True,
)
app.layout = dcc.Tabs(
    id="tabs", value='tab-0', children=[
        setup_page_components(),
    ]
)
set_page_container_style_display_contents()

if __name__ == "__main__":
    app.run_server(port=7777)
