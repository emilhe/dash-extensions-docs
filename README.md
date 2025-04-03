# dash-extensions-docs

Interactive documentation for the dash-extensions library

## Getting started

Make sure you have installed Python 3.12 and uv. Create new environment (for running locally),

```bash
uv venv && source .venv/bin/activate && uv sync
```

If you need to deploy any changes to dependencies, create a new `requirements.txt` (used by Render),

```bash
uv pip compile pyproject.toml -o requirements.txt
```
