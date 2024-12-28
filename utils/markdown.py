import os
from dash_down.html_renderer import DashHtmlRenderer
import dash_mantine_components as dmc
from box import Box
from dash_down.express import md_to_blueprint
from dash_down.mantine_renderer import DmcRenderer
from dash_extensions.enrich import html, DashBlueprint
from utils.ui import create_table_of_contents


# region Directives


def python_code(
    value: str, text: str, options: Box[str, str], blueprint: DashBlueprint
):
    with open(f"{value.replace('.', '/')}.py", "r") as f:
        source = f.readlines()
    return dmc.CodeHighlight("".join(source), language="python")


# endregion

# region Automatec toc genetation


def _record_link(self, children, level, links=None, original=None):
    links.append([children, level])
    return original(self, children=children, level=level)


class TocTracker:
    def __init__(self):
        self.links = None
        self._original = None

    def __enter__(self):
        self.links = []
        self._original = DmcRenderer.heading
        DmcRenderer.heading = (
            lambda s, c, l, links=self.links, original=self._original: _record_link(
                s, c, l, links, original
            )
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        DmcRenderer.heading = self._original


def str2anchor(children: str):
    string = str(children).lower()
    anchor = "".join(
        e if e.isalnum() else "" if i in [0, len(string) - 1] else "-"
        for i, e in enumerate(string)
    )
    return f"#a-{anchor}"


def md_to_blueprint_with_toc(pth: str, **md_options) -> DashBlueprint:
    with TocTracker() as at:
        blueprint = md_to_blueprint(CustomRenderer, pth, **md_options)
        blueprint.layout = html.Div(
            [
                blueprint.layout,
                create_table_of_contents(
                    [
                        (str2anchor(item[0]), item[0].replace(":", ""), "")
                        for item in at.links
                    ]
                ),
            ]
        )
    return blueprint


class CustomRenderer(DashHtmlRenderer):
    """
    Render markdown into Dash Mantine components.
    """

    def link(self, link, children=None, title=None):
        return dmc.Anchor(children, href=link)

    def image(self, src, alt="", title=None):
        # TODO: Review render (!)
        return dmc.Stack([dmc.Image(src=src, alt=alt), dmc.Text(title)])

    def heading(self, children, level):
        return dmc.Title(super().add_header_anchor(children), order=level)

    def thematic_break(self):
        return dmc.Divider()

    def block_code(self, children, info=None):
        lang = None
        if info is not None:
            info = info.strip()
        if info:
            lang = info.split(None, 1)[0]
        return dmc.CodeHighlight(children, language=lang)

    def block_quote(self, text):
        return dmc.Blockquote(text)

    def list(self, children, ordered, level, start=None):
        return dmc.List(children, type="ordered" if ordered else "unordered")

    def list_item(self, text, level):
        return dmc.ListItem(text)

    def table(self, text):
        return dmc.Table(text, striped=True, highlightOnHover=True)

    # NEW

    # def emphasis(self, text):
    #     return html.Em(text)

    # def strong(self, text):
    #     return html.Strong(text)

    def paragraph(self, text):
        return dmc.Text(text, className="m2d-paragraph")


# endregion


def camel(snake_str):
    return "".join(map(str.title, snake_str.split("_")))


def dash_proxy_shell(source, layout, render=True):
    code = [dmc.GridCol(dmc.CodeHighlight("".join(source), language="python"), span=1)]
    layout = html.Div(
        layout,
        style=dict(
            boxShadow="0px 3px 6px rgb(0 0 0 / 20%)", borderRadius="0px", padding="16px"
        ),
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
        style=dict(marginBottom="16px"),
    )


def blueprint_shell(children):
    return html.Div(
        children, style=dict(marginBottom="16px"), className="markdown-body"
    )


def register_pages(app, folder, order=None, order_map=None):
    md_options = dict(
        directives=[python_code],
        shell=blueprint_shell,
        dash_proxy_shell=dash_proxy_shell,
    )
    for fn in [fn for fn in os.listdir(folder) if fn.endswith(".md")]:
        name = fn.replace(".md", "")
        order = (
            order_map[name] if order_map is not None and name in order_map else order
        )
        blueprint = md_to_blueprint_with_toc(f"{folder}/{fn}", **md_options)
        blueprint.register(
            app,
            f"{folder}.{name}",
            prefix=name,
            name=camel(name),
            order=order,
            path=f"/{folder}/{name}",
        )
