import importlib
import mistletoe

from mistletoe import BaseRenderer
from dash import html
from dash_down.custom_token import CustomToken


class ApiDoc(CustomToken):
    def render(self, renderer: BaseRenderer, inner: str):
        # Parse api doc.
        module_name, component_name = ".".join(inner.split(".")[:-1]), inner.split(".")[-1]
        module = importlib.import_module(module_name)
        component = getattr(module, component_name)
        component_doc = component.__doc__
        docs = component_doc.split("Keyword arguments:")[-1]
        docs = docs.lstrip("\n\n")
        # Create tokens.
        heading_token = mistletoe.block_token.Heading((0, "Keyword Arguments"))
        heading_token.level = 5
        code_token = mistletoe.block_token.BlockCode(docs)
        code_token.language = "git"
        return html.Div([
            renderer.render_heading(heading_token),
            renderer.render_block_code(code_token)
        ])
