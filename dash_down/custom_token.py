import logging
from typing import List, TypeVar
from mistletoe import BaseRenderer


class CustomToken:  # pragma: no cover
    def render(self, renderer: BaseRenderer, inner: str):
        raise NotImplementedError


T = TypeVar('T', bound=BaseRenderer)
U = TypeVar('U', bound=CustomToken)


def bind_custom_tokens(renderer: T, custom_tokens: List[CustomToken]):
    # Create token mapping.
    custom_token_map = {}
    for t in custom_tokens:
        custom_token_map[t.__class__.__name__.replace("Token", "")] = t
    # Prepare monkey patching.
    render_quote_original = renderer.render_map['Quote']

    def render_quote(token):
        # TODO: What about this block?
        inner = [renderer.render(child) for child in token.children]
        # Check for custom elements.
        custom_element = _detect_custom_element(inner)
        if custom_element:
            return custom_element
        # If not found, just return normal block.
        return render_quote_original(token)

    def _detect_custom_element(inner):
        try:
            # Check for special elements.
            first_line = inner[0].children
            element_type = first_line.split(":")[0]
            if element_type in custom_token_map:
                # TODO: Add more elaborate parsing.
                args = first_line.split(":")[1:]
                kwargs = dict()
                return custom_token_map[element_type].render(renderer, *args, **kwargs)
        except Exception as e:
            logging.warning(str(e))
            return None
        return None

    renderer.render_map['Quote'] = render_quote
