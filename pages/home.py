import dash
import dash_mantine_components as dmc

from dash import html, dcc
from dash_down.express import md_to_blueprint_dmc

from utils.ui import create_table_of_contents

desc = "Dash Extensions is a collection of utility functions, syntax extensions, and Dash components that aim to " \
       "improve the Dash development experience"
dash.register_page(
    __name__,
    "/",
    title="Dash Extensions",
    description=desc,
)

content = md_to_blueprint_dmc("pages/home.md").layout
footer = dmc.Center(
    [
        dmc.Group(
            spacing="xs",
            children=[
                dmc.Text("Made by Emil Haldrup Eriksen"),
            ],
        )
    ]
)

layout = html.Div(
    [
        dmc.Container(
            size="lg",
            mt=30,
            children=[
                dmc.Stack(
                    align="center",
                    justify="center",
                    children=[
                        dmc.Image(src="/assets/dash_logo.png", width=250),
                        html.Div(
                            [
                                dmc.Text(
                                    desc, align="center",
                                )
                            ],
                            style={"width": 600},
                        ),
                        dcc.Link(
                            [
                                dmc.Button("Get Started"),
                            ],
                            href="/getting-started/installation",
                        ),
                    ],
                )
            ],
        ),
        dmc.Space(h=16),
        html.Div(dmc.Divider(), style=dict(width="100%")),
        dmc.Space(h=16),
        dmc.Container(content, size="lg", mt=30),
        dmc.Space(h=16),
        html.Div(dmc.Divider(), style=dict(width="100%")),
        dmc.Space(h=16),
        footer,
        create_table_of_contents([
                ("#features", "Features", ""),
                ("#contributors", "Contributors", ""),
            ])
    ]
)
