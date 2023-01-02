import dash_extensions
import dash_mantine_components as dmc
from collections import defaultdict
from dash_iconify import DashIconify
from dash_extensions.enrich import dcc, html, page_container, clientside_callback, Output, Input, State

IGNORE_SECTIONS = ["Getting Started", "Pages"]
HOME = f"Dash Extensions"
HOME_SHORT = "DE"
BADGE = dash_extensions.__version__
GITHUB_URL = "https://github.com/thedirtyfew/dash-extensions"
NAVBAR_ICONS = {
    "Components": "radix-icons:component-1",
    "Transforms": "radix-icons:transform",
}


# region Sourced from dmc docs: https://github.com/snehilvj/dmc-docs/blob/main/lib/appshell.py

def create_home_link(label):
    return dmc.Group([dmc.Anchor(
        label,
        size="xl",
        href="/",
        underline=False,
    ), dmc.Badge(
        BADGE,
        variant="outline",
        radius="xl",
    )])


def create_main_nav_link(icon, label, href):
    return dmc.Anchor(
        dmc.Group(
            [
                DashIconify(
                    icon=icon, width=23, color=dmc.theme.DEFAULT_COLORS["indigo"][5]
                ),
                dmc.Text(label, size="sm"),
            ]
        ),
        href=href,
        variant="text",
    )


def create_header_link(icon, href, size=22, color="indigo"):
    return dmc.Anchor(
        dmc.ThemeIcon(
            DashIconify(
                icon=icon,
                width=size,
            ),
            variant="outline",
            radius=30,
            size=36,
            color=color,
        ),
        href=href,
        target="_blank",
    )


def create_header(nav_data):
    return dmc.Header(
        height=70,
        fixed=True,
        px=25,
        children=[
            dmc.Stack(
                justify="center",
                style={"height": 70},
                children=dmc.Grid(
                    children=[
                        dmc.Col(
                            [
                                dmc.MediaQuery(
                                    create_home_link(HOME),
                                    smallerThan="lg",
                                    styles={"display": "none"},
                                ),
                                dmc.MediaQuery(
                                    create_home_link(HOME_SHORT),
                                    largerThan="lg",
                                    styles={"display": "none"},
                                ),
                            ],
                            span="content",
                            pt=12,
                        ),
                        dmc.Col(
                            span="auto",
                            children=dmc.Group(
                                position="right",
                                spacing="xl",
                                children=[
                                    dmc.MediaQuery(
                                        dmc.Select(
                                            id="select-component",
                                            style={"width": 250},
                                            placeholder="Search",
                                            nothingFound="No match found",
                                            searchable=True,
                                            clearable=True,
                                            data=[
                                                {
                                                    "label": component["name"],
                                                    "value": component["path"],
                                                }
                                                for component in nav_data
                                                if component["name"]
                                                   not in ["Home", "Not found 404"]
                                            ],
                                            icon=DashIconify(
                                                icon="radix-icons:magnifying-glass"
                                            ),
                                        ),
                                        smallerThan="md",
                                        styles={"display": "none"},
                                    ),
                                    create_header_link(
                                        "radix-icons:github-logo",
                                        GITHUB_URL,
                                    ),
                                    # create_header_link(
                                    #     "bi:discord", "https://discord.gg/KuJkh4Pyq5"
                                    # ),
                                    dmc.ActionIcon(
                                        DashIconify(
                                            icon="radix-icons:blending-mode", width=22
                                        ),
                                        variant="outline",
                                        radius=30,
                                        size=36,
                                        color="yellow",
                                        id="color-scheme-toggle",
                                    ),
                                    dmc.MediaQuery(
                                        dmc.ActionIcon(
                                            DashIconify(
                                                icon="radix-icons:hamburger-menu",
                                                width=18,
                                            ),
                                            id="drawer-hamburger-button",
                                            variant="outline",
                                            size=36,
                                        ),
                                        largerThan="lg",
                                        styles={"display": "none"},
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            )
        ],
    )


# NB: Heavily customized
def create_side_nave_content(nav_data):
    main_links = dmc.Stack(
        spacing="sm",
        mt=20,
        children=[
            create_main_nav_link(
                icon="material-symbols:rocket-launch-rounded",
                label="Getting Started",
                href="/getting_started/installation",
            ),
            create_main_nav_link(
                icon="material-symbols:javascript",
                label="Javascript",
                href="/getting_started/javascript",
            ),
            create_main_nav_link(
                icon="material-symbols:magic-button",
                label="Enrich",
                href="/getting_started/enrich",
            ),
        ],
    )
    # create component links
    sections = defaultdict(list)
    for entry in nav_data:
        label = entry["module"].split(".")[0]
        label = (" ".join(label.split("_"))).title()
        sections[label].append((entry["name"], entry["path"]))

    links = []
    for section, items in sorted(sections.items()):
        if section in IGNORE_SECTIONS:
            continue
        links.append(
            dmc.Divider(
                labelPosition="left",
                label=[
                    DashIconify(
                        icon=NAVBAR_ICONS[section], width=15, style={"marginRight": 10}
                    ),
                    section,
                ],
                my=20,
            )
        )
        links.extend(
            [
                dmc.Anchor(name, size="sm", href=path, variant="text")
                for name, path in items
            ]
        )

    return dmc.Stack(
        spacing="sm", children=[main_links, *links, dmc.Space(h=20)], px=25
    )


def create_side_navbar(nav_data):
    return dmc.Navbar(
        fixed=True,
        id="components-navbar",
        position={"top": 70},
        width={"base": 300},
        children=[
            dmc.ScrollArea(
                offsetScrollbars=True,
                type="scroll",
                children=create_side_nave_content(nav_data),
            )
        ],
    )


def create_navbar_drawer(nav_data):
    return dmc.Drawer(
        id="components-navbar-drawer",
        overlayOpacity=0.55,
        overlayBlur=3,
        zIndex=9,
        size=300,
        children=[
            dmc.ScrollArea(
                offsetScrollbars=True,
                type="scroll",
                style={"height": "100%"},
                pt=20,
                children=create_side_nave_content(nav_data),
            )
        ],
    )


def create_table_of_contents(toc_items):
    children = []
    for url, name, _ in toc_items:
        children.append(
            html.A(
                dmc.Text(name, color="dimmed", size="sm", variant="text"),
                style={"textTransform": "capitalize", "textDecoration": "none"},
                href=url,
            )
        )

    heading = dmc.Text("Table of Contents", mb=10, weight=500)
    toc = dmc.Stack([heading, *children], spacing=4, px=25, mt=20)

    return dmc.Aside(
        position={"top": 70, "right": 0},
        fixed=True,
        id="toc-navbar",
        width={"base": 300},
        zIndex=10,
        children=toc,
        withBorder=False,
    )


def create_app_shell(nav_data, children):
    clientside_callback(
        """ function(data) { return data } """,
        Output("mantine-docs-theme-provider", "theme"),
        Input("theme-store", "data"),
    )

    clientside_callback(
        """function(n_clicks, data) {
            if (data) {
                if (n_clicks) {
                    const scheme = data["colorScheme"] == "dark" ? "light" : "dark"
                    return { colorScheme: scheme } 
                }
                return dash_clientside.no_update
            } else {
                return { colorScheme: "light" }
            }
        }""",
        Output("theme-store", "data"),
        Input("color-scheme-toggle", "n_clicks"),
        State("theme-store", "data"),
    )

    # noinspection PyProtectedMember
    clientside_callback(
        """ function(children) { return null } """,
        Output("select-component", "value"),
        Input("_pages_content", "children"),
    )

    clientside_callback(
        """
        function(value) {
            if (value) {
                return value
            }
        }
        """,
        Output("url", "pathname"),
        Input("select-component", "value"),
    )

    clientside_callback(
        """function(n_clicks) { return true }""",
        Output("components-navbar-drawer", "opened"),
        Input("drawer-hamburger-button", "n_clicks"),
        prevent_initial_call=True,
    )

    return dmc.MantineProvider(
        dmc.MantineProvider(
            theme={
                "fontFamily": "'Inter', sans-serif",
                "primaryColor": "indigo",
                "components": {
                    "Button": {"styles": {"root": {"fontWeight": 400}}},
                    "Alert": {"styles": {"title": {"fontWeight": 500}}},
                    "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
                },
            },
            inherit=True,
            children=[
                         dcc.Store(id="theme-store", storage_type="local"),
                         dcc.Location(id="url"),
                         dmc.NotificationsProvider(
                             [
                                 create_header(nav_data),
                                 create_side_navbar(nav_data),
                                 create_navbar_drawer(nav_data),
                                 html.Div(
                                     dmc.Container(size="lg", pt=90, children=page_container),
                                     id="wrapper",
                                 ),
                             ]
                         ),
                     ] + children,
        ),
        theme={"colorScheme": "light"},
        id="mantine-docs-theme-provider",
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )

# endregion
