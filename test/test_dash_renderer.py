from mistletoe import Document
from dash_down.custom_token import bind_custom_tokens
from dash_down.doc_tokens import ApiDocToken
from dash_down.html_renderer import DashHtmlRenderer


def test_dash_html_renderer():
    with open('markdown_test.md', 'r') as f:
        with DashHtmlRenderer() as r:
            bind_custom_tokens(r, custom_tokens=[ApiDocToken()])
            p = r.render(Document(f))
