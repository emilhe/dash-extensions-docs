from dash_down.express import render_markdown_html, render_markdown_dmc


def test_render_markdown_html():
    blueprint = render_markdown_html('markdown_test.md')
    # TODO: Maybe add UI validation, e.g. using Percy


def test_render_markdown_dmc():
    blueprint = render_markdown_dmc('markdown_test.md')
    # TODO: Maybe add UI validation, e.g. using Percy
