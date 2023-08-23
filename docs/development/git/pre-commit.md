# Pre-commit

It is a tool to easily setup and run `pre-commit hooks` for your git repository.<br>
See the documentation of [pre-commit](https://pre-commit.com/) for further information.<br>
It is used to improve auto-format code, do linting and run tests before every commit.

## Install

Install the required package in a python environment. <br>
💻 `pip install pre-commit` install pre-commit <br>
💻 `pre-commit install` install pre-commit

## Setup

The hooks are configured in the `.pre-commit-config.yaml` file.

### List of implemented hooks

- [Pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) - Out-of-the-box hooks
- [Black](https://github.com/psf/black) - Python code formatter
- [isort](https://github.com/pycqa/isort) - Sort Python imports
- [Ruff](https://github.com/astral-sh/ruff-pre-commit) - Fast Python linter, written in Rust
- [Flake8](https://github.com/pycqa/flake8) - Python linter with PyFlakes and pycodestyle
- [mypy mirror](https://github.com/pre-commit/mirrors-mypy) - Added static types to Python
- [mirrors-prettier](https://github.com/pre-commit/mirrors-prettier) - Formatting for other files then python scripts

## Run

All commits will trigger the hooks automatically.<br>
💠 `git commit file -m "Commit message #IssueNr"` to commit

Commit without running the hooks.<br>
💠 `git commit --no-verify file` to commit without hooks

!!! Note
There can be problems with file line endings on Windows, `CRLF` is used on Windows and `LF` is used on Linux.

To run the hooks on all files in your repository use:<br>
💻 `pre-commit run --all-files`

!!! Warning
If the hook is applied to markdown files that include special formatting,
(e.g. `mkdocs.yml`), this can introduce incorrect changes.
