import os

import dash_mantine_components as dmc
from dash_down.express import DmcRenderer, md_to_blueprint
from dash_extensions.enrich import DashBlueprint, PrefixIdTransform, html

from utils.ui import create_table_of_contents

# region Directives


def python_code(value: str, text: str, options: dict[str, str], blueprint: DashBlueprint):
    with open(f"{value.replace('.', '/')}.py", "r") as f:
        source = f.readlines()
    return dmc.CodeHighlight("".join(source), language="python", mb=16)


# endregion

# region Automatic toc genetation


def _record_link(self, children, level, links, original):
    links.append([children, level])
    return original(self, children=children, level=level)


class TocTracker:
    def __init__(self):
        self.links = None
        self._original = None

    def __enter__(self):
        self.links = []
        self._original = DmcRenderer.heading
        DmcRenderer.heading = lambda s, c, l, links=self.links, original=self._original: _record_link(
            s, c, l, links, original
        )  # type: ignore
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        DmcRenderer.heading = self._original  # type: ignore


def str2anchor(children: str):
    string = str(children).lower()
    anchor = "".join(e if e.isalnum() else "" if i in [0, len(string) - 1] else "-" for i, e in enumerate(string))
    return f"#a-{anchor}"


def md_to_blueprint_with_toc(pth: str, **md_options) -> DashBlueprint:
    with TocTracker() as at:
        blueprint = md_to_blueprint(DmcRenderer, pth, **md_options)
        blueprint.layout = html.Div(
            [
                blueprint.layout,
                create_table_of_contents([(str2anchor(item[0]), item[0].replace(":", ""), "") for item in at.links]),
            ]
        )
    return blueprint


# endregion


def camel(snake_str):
    return "".join(map(str.title, snake_str.split("_")))


def dash_proxy_shell(source, layout, render=True):
    code = [dmc.GridCol(dmc.CodeHighlight("".join(source), language="python"), span=1)]
    layout = html.Div(
        layout,
        style=dict(boxShadow="0px 3px 6px rgb(0 0 0 / 20%)", borderRadius="0px", padding="16px"),
    )
    app_layout = [
        dmc.GridCol(
            layout,
            span=1,
            style=dict(paddingLeft="8px", paddingRight="8px", marginTop="-14px"),
        )
    ]
    return dmc.Grid(
        code + (app_layout if render else []),
        columns=1,
        mb=16,
    )


def register_pages(app, folder, order=None, order_map=None):
    md_options = dict(
        directives=[python_code],
        dash_proxy_shell=dash_proxy_shell,
    )
    for fn in [fn for fn in os.listdir(folder) if fn.endswith(".md")]:
        name = fn.replace(".md", "")
        order = order_map[name] if order_map is not None and name in order_map else order
        blueprint = md_to_blueprint_with_toc(f"{folder}/{fn}", **md_options)
        blueprint.register(
            app,
            f"{folder}.{name}",
            prefix=PrefixIdTransform(name, escape=prefix_escape),
            name=camel(name),
            order=order,
            path=f"/{folder}/{name}",
        )


def prefix_escape(component_id: str):
    if isinstance(component_id, str):
        if component_id.startswith("a-"):  # intended usage is for anchors
            return True
        if component_id.startswith("anchor-"):  # intended usage is for anchors
            return True
        if component_id.startswith("div_log_handler"):  # for logging utilities
            return True
        if component_id.startswith("event_store"):  # for event flows
            return True
        if component_id.startswith("notifications_log_handler"):  # for logging utilities
            return True
    return False
