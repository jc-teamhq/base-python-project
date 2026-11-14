# base-python-project

A [Copier](https://copier.readthedocs.io/) template for a minimal,
fully-typed Python project on the [Astral](https://astral.sh) toolchain:
uv, ruff and ty, plus pytest with coverage, pre-commit hooks, and a
portable CI script that runs on any CI system.

## Create a project

```bash
uvx copier copy <path-or-git-url-of-this-repo> my-project
```

Copier asks:

| Question       | Used for                                                    | Default                    |
| -------------- | ----------------------------------------------------------- | -------------------------- |
| `project_name` | distribution name and CLI command (e.g. `my-project`)       | —                          |
| `package_name` | importable package (e.g. `my_project`)                      | from `project_name`        |
| `description`  | `pyproject.toml` and the README                             | a generic one-liner        |
| `author_name`  | `pyproject.toml` and the copyright notice                   | —                          |
| `license`      | GPL-3.0-or-later, GPL-3.0-only, MIT, Apache-2.0, or Proprietary (no license file; blocks PyPI uploads) | GPL-3.0-or-later |

Then follow the next steps Copier prints (`git init`, `uv sync`,
`uv run pre-commit install`). The generated project's README documents
everything else: layout, common commands, CI, and configuration.

## Update a generated project

Generated projects record their answers in `.copier-answers.yml`, so they
can pull in later template changes. From inside the generated project:

```bash
uvx copier update
```

Copier uses this repo's latest git tag (or `HEAD` if there are none), so
tag template releases (e.g. `v1.0.0`) to make updates deliberate.

## Developing the template

```
.
├── copier.yml                # questions and template settings
├── pyproject.toml            # pins Copier (via uv.lock) for developing the template
├── scripts/
│   └── test-template.sh      # generates projects and runs their CI
└── template/                 # becomes the generated project
    ├── pyproject.toml.jinja  # `.jinja` files are rendered; others are copied as-is
    ├── src/{{ package_name }}/
    └── ...
```

- Files ending in `.jinja` are rendered with the answers (the suffix is
  dropped); everything else is copied verbatim.
- Directory and file names can use answers too, e.g.
  `src/{{ package_name }}/`. A name that renders empty is skipped, which is
  how only the chosen license's `LICENSE` file is generated.

Because the Python in `template/` is mostly Jinja, it can't be linted or
tested in place. Test it by generating projects instead:

```bash
uv sync
scripts/test-template.sh
```

The script uses the working tree (uncommitted changes included). It checks
that each license choice renders and builds, that no unrendered Jinja is
left behind, and runs the default project's full `scripts/ci.sh`. It is
also the CI command for this repo.

## License

This template is licensed under GPL-3.0-or-later; see `LICENSE`.
