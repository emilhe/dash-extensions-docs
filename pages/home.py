import dash
import dash_mantine_components as dmc

from dash import html, dcc

desc = "Dash Extensions is a collection of utilities functions, syntax extensions, and dash components that aim to " \
       "improve the Dash development experience."
dash.register_page(
    __name__,
    "/",
    description=desc,
)

banner_layout = html.Div(
    [
        dmc.Paper(
            padding="xl",
            children=[
                dmc.Center(
                    dmc.Group(
                        direction="column",
                        position="center",
                        children=[
                            # dmc.Image(src="/assets/logo.png", width=250),
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
                )
            ],
        ),
        dmc.Space(h=10),
    ]
)

some_feature = html.Div(
    "SOME FEATURE GOES HERE"
)

layout = [
    banner_layout,
    some_feature,
]
