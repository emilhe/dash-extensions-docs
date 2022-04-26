## Installation

The preferred way to install `dash-extensions` is via pip,

```bash
pip install dash-extensions
```

or if you are using [Poetry](https://python-poetry.org),

```bash
poetry add dash-extensions
```

or if your environment is managed by [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/packages.html),

```bash
mamba install -c conda-forge dash-extensions
conda install -c conda-forge dash-extensions
```

### Example

It should now be possible to run the following (minimal) example app,

.. dash-proxy:: getting_started.minimal

### Optional dependencies

Other recommended/related packages include

* [`dash-mantine-components`](https://www.dash-mantine-components.com/) for creating user interfaces in Dash
* [`dash-iconify`](https://www.dash-mantine-components.com/getting-started/dash-iconify) for creating icons in Dash
* [`dash-leaflet`](https://github.com/thedirtyfew/dash-leaflet) for creating map visualizations in Dash
* [`dash-down`](https://github.com/emilhe/dash-down) for converting markdown to Dash applications

This documentation is itself a Dash app created using `dash-mantine-components`, `dash-iconify`, and `dash-down`.



