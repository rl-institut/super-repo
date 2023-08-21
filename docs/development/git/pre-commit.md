# Pre-commit

It is a tool to easily setup and run `pre-commit hooks` for your git repository.
See the documentation of [pre-commit](https://pre-commit.com/) for further information.
It is used to improve auto-format code, do linting and run tests before every commit.

## Install

Install the required package in a python environment. <br>
💻 `pip install pre-commit` install pre-commit <br>
💻 `pre-commit install` install pre-commit

## Setup

The hooks are configured in the `.pre-commit-config.yaml` file.

### List of useful hooks:

Python code style formatter

    https://github.com/psf/black

Sort Python imports

    https://github.com/pycqa/isort

Very fast python linter implemented useing Rust

    https://github.com/charliermarsh/ruff-pre-commit

Python linter

    https://github.com/pycqa/flake8

Added static types to Python (Python is dynamically typed)

    https://github.com/pre-commit/mirrors-mypy

## Run

All commits will trigger the hooks automatically.
💠 `git commit file` to commit

If you don't want to run the hooks you can use
💠 `git commit --no-verify file` to commit without hooks

!!! Note
There can be problems with file line endings on Windows, CRLF is used on Windows and LF is used on Linux.
LF is also maintained on platforms like GitHub.

To run the hooks on all files in your repository use:
💻 `pre-commit run --all-files`
