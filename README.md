<!--
USING THIS TEMPLATE:

1. Update the package name:
  a. Replace "thispackage-fullname" with the human-readable name of the package (i.e., with casing, spaces, etc.).
  b. Replace "thispackage-name" with the package's name as it will be shown in GitHub and the package manager (i.e., `pip install thispackage-name`).
  c. Replace "thispackage" with the package's name as it will be referenced and imported (e.g., `import thispackage`). Rename the `./thispackage` directory to match.
2. Populate the remaining template fields in:
  a. README.md
  b. AGENTS.md
  c. pyproject.toml
  d. thispackage/_version.py
-->

# thispackage-name

[![PyPI][pypi-img]][pypi-lnk]
[![License][license-img]][license-lnk]
[![Tests][tests-img]][tests-lnk]
[![Code Style][codestyle-img]][codestyle-lnk]
[![Coverage Status][codecov-img]][codecov-lnk]

`thispackage-name` is <!-- what is the project -->. The project provides <!-- what is the project for -->.

## Overview

<!-- background info -->. This project focuses on providing:

- <!-- list of high-level features -->

## Installation

### From PyPI

```bash
pip install thispackage-name
```

or, with [astral-uv](https://docs.astral.sh/uv/):

```bash
uv add thispackage-name
```

### From source

```bash
git clone https://github.com/your-username/thispackage-name.git
cd thispackage-name
pip install .
```

## Quickstart

1. <!-- numbered quickstart guide -->a

```python
# sample usage code block
```

### other high-level use-case/feature quickstarts

### use-case/feature

<!-- short description -->

```python
# sample usage code block
```

## Developer Guide

- **Package Manager**: [`uv`](https://docs.astral.sh/uv/)
- **Language Server**: [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- **Static Type Checker**: [`basedpyright`](https://github.com/detachhead/basedpyright)
- **Linter**: [Ruff Linter](https://docs.astral.sh/ruff/linter/)
- **Code Formatter**: [Ruff Formatter](https://docs.astral.sh/ruff/formatter/)

Set up a development environment with [`uv`](https://docs.astral.sh/uv/):

```bash
uv sync --all-extras --all-groups
uv run pytest tests

uv run ruff check
uv run ruff format
```

### Key Development Principles

<!-- add additional principles (keep minimal) -->

- Maintain 100% passing tests, at least 80% test coverage, formatting, and linting before opening a pull request.
- Update docstrings alongside code changes to keep the generated reference accurate.

### Document Generation

Documentation is generated using [MkDocs](https://www.mkdocs.org/). The technical reference surfaces the reStructuredText style docstrings from the package's source code.

```bash
uv sync --group docs

# Run the development server
uv run mkdocs serve -f mkdocs/mkdocs.yaml
# Build the static site
uv run mkdocs build -f mkdocs/mkdocs.yaml
```

## Contributing

Contributions are welcome! To get started:

1. Fork the repository and create a new branch.
2. Install development dependencies (see the [developer guide](#developer-guide)).
3. Add or update tests together with your change.
4. Run the full test, linting, and formatting suite locally.
5. Submit a pull request describing your changes and referencing any relevant issues.

For major changes, open an issue first to discuss your proposal.

## Design

The software design architecture prioritizes <!-- design priorities -->, ensuring <!-- justification -->.

- **Design element**: <!-- description -->, so that <!-- justification -->

## License

Distributed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). See [LICENSE](LICENSE) for details.

## Contact

Questions or issues? Please open an issue on the repository's issue tracker.

<!-- Badges -->

[pypi-lnk]: https://pypi.org/p/thispackage-name
[pypi-img]: https://img.shields.io/pypi/v/thispackage-name.svg
[tests-lnk]: https://github.com/paddy74/thispackage-name/actions/workflows/ci.yaml
[tests-img]: https://img.shields.io/github/actions/workflow/status/paddy74/thispackage-name/ci.yaml?logo=github&label=tests&branch=main
[codecov-lnk]: https://codecov.io/github/paddy74/thispackage-name
[codecov-img]: https://codecov.io/github/paddy74/thispackage-name/graph/badge.svg?token=IH3MTBANTT
[codestyle-lnk]: https://docs.astral.sh/ruff
[codestyle-img]: https://img.shields.io/badge/code%20style-ruff-000000.svg
[license-lnk]: ./LICENSE
[license-img]: https://img.shields.io/pypi/l/thispackage-name?color=light-green&logo=gplv3&logoColor=white
