import os
import dash_mantine_components as dmc

from box import Box
from dash_down.directives import DashDirective
from dash_down.express import md_to_blueprint_dmc
from dash_extensions.enrich import html, DashBlueprint


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


def register_folder(app, folder, plugins, order=None):
    for fn in [fn for fn in os.listdir(folder) if fn.endswith(".md")]:
        name = fn.replace('.md', '')
        blueprint = md_to_blueprint_dmc(f"{folder}/{fn}", plugins=plugins)
        blueprint.register(app, f"pages.{folder}.{name}", prefix=name, name=camel(name), order=order)
