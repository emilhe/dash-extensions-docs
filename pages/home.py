import dash
import dash_mantine_components as dmc

from dash import html, dcc
from dash_down.express import md_to_blueprint_dmc

desc = "Dash Extensions is a collection of utility functions, syntax extensions, and Dash components that aim to " \
       "improve the Dash development experience"
dash.register_page(
    __name__,
    "/",
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
        dmc.Paper(
            children=[
                dmc.Center(
                    dmc.Group(
                        direction="column",
                        position="center",
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
                                href="/pages/getting-started/installation",
                            ),
                        ],
                    )
                )
            ],
        ),
        dmc.Space(h=16),
        html.Div(dmc.Divider(), style=dict(width="100%")),
        dmc.Space(h=16),
        content,
        dmc.Space(h=16),
        html.Div(dmc.Divider(), style=dict(width="100%")),
        dmc.Space(h=16),
        footer
    ]
)
