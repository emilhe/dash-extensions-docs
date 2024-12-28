from os import environ

import dash
import dash_mantine_components as dmc
import requests

from dash import html
from dash_down.express import md_to_blueprint_dmc
from dash_iconify import DashIconify

from utils.ui import create_table_of_contents

desc = (
    "Dash Extensions is a collection of utility functions, syntax extensions, and Dash components that aim to "
    "improve the Dash development experience"
)
dash.register_page(
    __name__,
    "/",
    title="Dash Extensions",
    description=desc,
)


def create_title(title, id):
    return dmc.Text(title, ta="center", style={"fontSize": 30}, id=id)


def create_head(text):
    return dmc.Text(text, ta="center", my=10, mx=0)


def create_contributors_avatars():
    resp = requests.get(
        "https://api.github.com/repos/thedirtyfew/dash-extensions/contributors",
        headers={"authorization": f"token {environ['CONTRIB_TOKEN']}"},
    )
    contributors = resp.json()
    children = []
    for user in contributors:
        print(type(user))
        print(user)
        avatar = dmc.Tooltip(
            dmc.Anchor(dmc.Avatar(src=user["avatar_url"]), href=user["html_url"]),
            label=user["login"],
            position="bottom",
        )
        children.append(avatar)

    return dmc.Group(children, position="center", id="contributors")


content = md_to_blueprint_dmc("pages/home.md").layout
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
                        dmc.Image(src="/assets/dash_logo.png", w=250),
                        html.Div(
                            [
                                dmc.Text(
                                    desc,
                                    ta="center",
                                )
                            ],
                            style={"maxWidth": 600},
                        ),
                        # dcc.Link(
                        #     [
                        #         dmc.Button("Let"),
                        #     ],
                        #     href="/getting-started/installation",
                        # ),
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
        # create_title("Contributors", id="contributors"),
        (create_contributors_avatars() if "CONTRIB_TOKEN" in environ else None),
        dmc.Space(h=16),
        html.Div(dmc.Divider(), style=dict(width="100%")),
        dmc.Space(h=16),
        dmc.Center(
            dmc.Group(
                gap="xs",
                children=[
                    dmc.Text("Made with"),
                    DashIconify(icon="akar-icons:heart", width=19, color="red"),
                    dmc.Text("by Emil Haldrup Eriksen"),
                ],
            )
        ),
        create_table_of_contents(
            [
                ("#contributors", "Contributors", ""),
            ]
        ),
    ]
)
