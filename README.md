# base-python-project

A minimal, fully-typed Python project template wired up with the
[Astral](https://astral.sh) toolchain:

- **[uv](https://docs.astral.sh/uv/)** — packaging, virtualenv, and dependency management
- **[ruff](https://docs.astral.sh/ruff/)** — linting and formatting
- **[ty](https://docs.astral.sh/ty/)** — type checking
- **[pytest](https://docs.pytest.org/)** + **[pytest-cov](https://pytest-cov.readthedocs.io/)** — testing and coverage
- **[pre-commit](https://pre-commit.com/)** — runs the checks on every commit

## Layout

```
.
├── .pre-commit-config.yaml # lint/format/type-check hooks (also used by CI)
├── pyproject.toml          # project metadata + tool config (ruff, ty, pytest, coverage)
├── uv.lock                 # locked dependency versions (commit this)
├── src/
│   └── base_python_project/
│       ├── __init__.py
│       ├── __main__.py     # CLI entry point (`base-python-project`)
│       ├── core.py
│       └── py.typed        # marks the package as typed (PEP 561)
└── tests/
    ├── test_core.py
    └── test_main.py
```

A `src/` layout is used so that tests run against the installed package
rather than the working directory, catching packaging mistakes early.

## Getting started

```bash
uv sync                         # create .venv and install everything (incl. dev tools)
uv run pre-commit install       # run the checks automatically on every commit
uv run base-python-project      # -> Hello, world!  (or: uv run python -m base_python_project)
```

`uv sync` reads `pyproject.toml` + `uv.lock` and builds a reproducible
environment in `.venv`. You never need to activate it manually — prefix
commands with `uv run`.

## Common tasks

```bash
uv run pre-commit run --all-files   # all static checks: lock, lint, format, types
uv run ruff check .
uv run ruff format .
uv run ty check
uv run pytest                       # tests + coverage (fails below 90%)
```

## Continuous integration

The checks live in the repo, not in any CI provider's config, so any CI
system (GitLab CI, Bitbucket Pipelines, Forgejo/Gitea Actions, Jenkins, …)
only needs [uv](https://docs.astral.sh/uv/getting-started/installation/)
installed and these commands:

```bash
uv sync --locked
uv run pre-commit run --all-files
uv run --isolated --python 3.12 pytest   # repeat for each supported version:
uv run --isolated --python 3.13 pytest   # 3.12 is the minimum (`requires-python`)
uv run --isolated --python 3.14 pytest
```

`--isolated` runs the tests in a throwaway environment for that interpreter,
so the project `.venv` is left untouched.

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
- `[tool.pytest]` (pytest's native TOML config, with `strict = true`)
- `[tool.coverage.run]` / `[tool.coverage.report]`

Adjust the selected ruff rule set and ty rule severities there to match
your team's preferences.
