# base-python-project

A minimal, fully-typed Python project template wired up with the
[Astral](https://astral.sh) toolchain:

- **[uv](https://docs.astral.sh/uv/)** — packaging, virtualenv, and dependency management
- **[ruff](https://docs.astral.sh/ruff/)** — linting and formatting
- **[ty](https://docs.astral.sh/ty/)** — type checking
- **[pytest](https://docs.pytest.org/)** — testing

## Layout

```
.
├── pyproject.toml          # project metadata + tool config (ruff, ty, pytest)
├── src/
│   └── base_python_project/
│       ├── __init__.py
│       ├── __main__.py     # `python -m base_python_project`
│       ├── core.py
│       └── py.typed        # marks the package as typed (PEP 561)
└── tests/
    └── test_core.py
```

A `src/` layout is used so that tests run against the installed package
rather than the working directory, catching packaging mistakes early.

## Getting started

```bash
uv sync                 # create .venv and install everything (incl. dev tools)
uv run python -m base_python_project   # -> Hello, world!
```

`uv sync` reads `pyproject.toml` + `uv.lock` and builds a reproducible
environment in `.venv`. You never need to activate it manually — prefix
commands with `uv run`.

## Common tasks

```bash
uv run ruff check .
uv run ruff format .
uv run ty check
uv run pytest
```

## Managing dependencies

```bash
uv add requests            # add a runtime dependency
uv add --dev mypy          # add a dev-only dependency
uv remove requests         # remove one
uv lock --upgrade          # refresh the lockfile
```

## Configuration

All tool configuration lives in `pyproject.toml`:

- `[tool.ruff]` / `[tool.ruff.lint]` / `[tool.ruff.format]`
- `[tool.ty.environment]` / `[tool.ty.src]` / `[tool.ty.rules]`
- `[tool.pytest.ini_options]`

Adjust the selected ruff rule set and ty rule severities there to match
your team's preferences.
