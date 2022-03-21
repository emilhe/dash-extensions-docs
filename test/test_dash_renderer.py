import mistletoe

from dash_down.html_renderer import DashHtmlRenderer


def test_dash_html_renderer():
    with open('markdown_test.md', 'r') as fin:
        bp = mistletoe.markdown(fin, DashHtmlRenderer)
