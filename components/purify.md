### Purify

The `Purify` component makes it possible to render HTML, MathML, and SVG. Typically, such rendering is prone to XSS vulnerabilities. These risks are mitigated by sanitizing the html input using the [DOMPurify](https://github.com/cure53/DOMPurify) library. Here is a minimal example,

.. dash-proxy:: components.purify

.. api-doc:: dash_extensions.Purify