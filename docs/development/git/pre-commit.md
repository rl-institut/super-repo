# Check the code by using pre-commit


We use pre-commit hooks to check code quality on a regular basis.
We need to run the hooks at least once for each release.

## What code-quality checks do we use

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

## Setup

The hooks are configured in the `.pre-commit-config.yaml` file.

!!! Warning
    Add create config guide.


To run all checks you have to install pre-commit.

    pip install pre-commit

Then install all hook environments.

    pre-commit install

!!! Info
    This will take a wile but all environments will be reused.

Now all commits will trigger the hooks automatically.

    git commit -m "Commit" some-file

If you dont want to run the hooks you can either deactevate them or use:

    git commit --no-verify -m "Your commit message"

!!! Note
    There can be problems with file line endings on Windows, CRLF is used on Windows and LF is used on Linux.
    LF is also maintained on platforms like GitHub.

To runn the hooks on all files in your repository use:

    pre-commit run --all-files

!!! Warning
    This hook will also run on markdown files. If the markdown files include special formatting, such as those provided by mkdocs-materials, this can potentially misformat the document. Please be aware that applying this command to markdown files can introduce incorrect changes. Apply it carefully.
