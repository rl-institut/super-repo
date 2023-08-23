# Configure Continuous Integration using GitHub Actions

## What is included in the tests?

Our continuous integration (CI) process executes a series of tests, including running `pytest` and performing linting and code quality checks.

Here's an overview of the tasks involved in our example:

- Running `pytest`
- Checking code syntax with `black`
- Verifying `docstrings` with `flake8`
- Sorting imports with `isort`

All these tools are executed as part of a job defined within a GitHub Actions workflow file. The workflow defines the tasks for a job, and a runner executes these tasks on a virtual machine provided by GitHub.

!!! Info "Setup GitHub Actions"
    To set up GitHub Actions workflows for your repository, follow the [official GitHub guide](https://docs.github.com/en/actions/guides).

Our CI workflow is triggered whenever there's a pull request or a commit to the `develop` or `production` branches. The workflow prepares the Python environment and installs relevant dependencies before executing the `tox` automation suite. If any errors are detected, the workflow fails and generates a detailed report for developers to review.
