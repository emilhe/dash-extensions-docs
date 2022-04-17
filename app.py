import os
import dash_labs as dl
import dash
import dash_extensions
import dash_mantine_components as dmc

from box import Box
from dash_down.directives import DashProxyDirective, DashDirective
from dash_down.plugins import PluginBlueprint
from dash_iconify import DashIconify
from collections import defaultdict
from dash_extensions.enrich import dcc, html, DashProxy, DashBlueprint
from dash_down.express import md_to_blueprint_dmc


# region Layout

def layout(children):
    return dmc.MantineProvider(
        theme={"colorScheme": "light"},
        withGlobalStyles=True,
        withNormalizeCSS=True,
        children=[
            dmc.NotificationsProvider(
                [
                    dmc.Container(
                        fluid=True,
                        px="lg",
                        style={"marginTop": 90},
                        children=[
                            html.Div(
                                id="dummy-container-for-header-select",
                                style={"display": "none"},
                            ),
                            html.Div(
                                id="home-notifications-container",
                                style={"display": "none"},
                            ),
                            page_header(),
                            side_nav(),
                            dmc.Container(
                                px="lg",
                                id="main-content",
                                children=children,
                            ),
                        ],
                    )
                ]
            )
        ],
    )


def page_header():
    return dmc.Header(
        height=70,
        fixed=True,
        p="md",
        children=[
            dmc.Group(
                position="apart",
                style={"marginLeft": 20, "marginRight": 20},
                children=[
                    dmc.Group(
                        [
                            # dmc.Image(src="/assets/logo_header.png", width=30),
                            dcc.Link(
                                dmc.Text(
                                    "Dash Extensions", color="dark", size="xl"
                                ),
                                href="/",
                                style={"textDecoration": "none"},
                            ),
                            dmc.Badge(
                                dash_extensions.__version__,
                                color="gray",
                                variant="outline",
                                radius="xl",
                            ),
                            # html.A(
                            #     dmc.Image(
                            #         src="https://img.shields.io/pypi/v/dash-extensions.svg", radius="xl"
                            #     ), href="https://pypi.org/project/dash-extensions/"
                            # )

                        ]
                    ),
                    dmc.Group(
                        position="right",
                        children=[
                            html.A(
                                dmc.Button(
                                    dmc.Text(
                                        "Source Code",
                                        color="dark",
                                        weight="lighter",
                                        size="sm",
                                    ),
                                    radius="xl",
                                    variant="light",
                                    color="gray",
                                    rightIcon=[
                                        DashIconify(
                                            icon="radix-icons:github-logo",
                                            color="black",
                                            width=20,
                                        )
                                    ],
                                ),
                                href="https://github.com/thedirtyfew/dash-extensions",
                                className="hide-sm",
                            ),
                            html.A(
                                dmc.Button(
                                    dmc.Text(
                                        "Docs",
                                        color="dark",
                                        weight="lighter",
                                        size="sm",
                                    ),
                                    radius="xl",
                                    variant="light",
                                    color="gray",
                                    rightIcon=[
                                        DashIconify(
                                            icon="radix-icons:github-logo",
                                            color="black",
                                            width=20,
                                        )
                                    ],
                                ),
                                href="https://github.com/emilhe/dash-extensions-docs",
                                className="hide-sm",
                            ),
                            # html.A(
                            #     dmc.Button(
                            #         dmc.Text(
                            #             "Discord",
                            #             color="dark",
                            #             weight="lighter",
                            #             size="sm",
                            #         ),
                            #         radius="xl",
                            #         variant="light",
                            #         color="gray",
                            #         rightIcon=[
                            #             DashIconify(
                            #                 icon="fa-brands:discord",
                            #                 width=20,
                            #                 color="#7289da",
                            #             )
                            #         ],
                            #     ),
                            #     href="https://discord.gg/KuJkh4Pyq5",
                            #     className="hide-sm",
                            # ),
                            dmc.Select(
                                id="select-component",
                                style={"width": 300},
                                placeholder="Search",
                                nothingFound="No match found",
                                searchable=True,
                                clearable=True,
                                icon=[DashIconify(icon="radix-icons:magnifying-glass")],
                                data=[
                                    {
                                        "label": component["name"],
                                        "value": component["name"],
                                    }
                                    for component in dash.page_registry.values()
                                    if component["module"] not in ["pages.home"]
                                ],
                            ),
                        ],
                    ),
                ],
            )
        ],
    )


def side_nav():
    sections = defaultdict(list)
    for entry in dash.page_registry.values():
        label = entry["module"].split(".")[1]
        label = (" ".join(label.split("-"))).title()
        sections[label].append((entry["name"], entry["path"]))

    children = []
    for section, pages in sorted(sections.items(), reverse=True):
        if section not in ["Home"]:
            component = dmc.Accordion(
                state={"0": True},
                iconPosition="right",
                icon=[DashIconify(icon="radix-icons:chevron-down")],
                children=[
                    dmc.AccordionItem(
                        label=section,
                        children=[
                            dmc.Group(
                                direction="column",
                                spacing="xs",
                                children=[
                                    dcc.Link(
                                        dmc.Text(name, size="sm", color="gray"),
                                        href=path,
                                        id=name,
                                        style={"textDecoration": "none"},
                                    )
                                    for name, path in pages
                                ],
                            )
                        ],
                    )
                ],
            )
            children.append(component)

    return dmc.Navbar(
        id="components-navbar",
        fixed=True,
        position={"top": 70},
        width={"base": 250},
        children=[
            dmc.ScrollArea(
                style={"height": "calc(100% - 70px)"},
                offsetScrollbars=True,
                type="scroll",
                children=children,
            )
        ],
    )


# endregion

# region Utils (to be moved?)

def camel(snake_str):
    return ''.join(map(str.title, snake_str.split('_')))


def custom_code_renderer(source, layout, render=True):
    code = [dmc.Col(dmc.Prism("".join(source), language="python"), span=1)]
    layout = html.Div(layout, style=dict(boxShadow="0px 3px 6px rgb(0 0 0 / 20%)", borderRadius="0px", padding="16px"))
    app_layout = [dmc.Col(layout, span=1, style=dict(paddingLeft="8px", paddingRight="8px", marginTop="-14px"))]
    return dmc.Grid(code + (app_layout if render else []), columns=1, style=dict(marginBottom="16px"))


class PythonDirective(DashDirective):
    def render_directive(self, value: str, text: str, options: Box[str, str], blueprint: DashBlueprint):
        with open(f"{value.replace('.', '/')}.py", 'r') as f:
            source = f.readlines()
        return dmc.Prism("".join(source), language="python")


def register_folder(folder):
    for fn in [fn for fn in os.listdir(folder) if fn.endswith(".md")]:
        name = fn.replace('.md', '')
        blueprint = md_to_blueprint_dmc(f"{folder}/{fn}", plugins=[dpd, PythonDirective()])
        blueprint.register(app, camel(f"pages.{folder}.{name}"), prefix=name)


# endregion


# dp = PluginBlueprint(layout=lambda x: html.Div(x, className="light markdown-body"))
app = DashProxy(plugins=[dl.plugins.pages])
dpd = DashProxyDirective(custom_render=custom_code_renderer)
# Register component blueprints.
register_folder("components")
register_folder("transforms")
# for fn in [fn for fn in os.listdir("components") if fn.endswith(".md")]:
#     name = fn.replace('.md', '')
#     blueprint = md_to_blueprint_dmc(f"components/{fn}", plugins=[dpd, PythonDirective()])
#     blueprint.register(app, camel(f"blueprints.components.{name}"), prefix=name)
# Bind layout.
app.layout = layout(dl.plugins.page_container)

if __name__ == '__main__':
    app.run_server(port=7879)
