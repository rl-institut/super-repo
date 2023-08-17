# Continuous Integration with GitHub

Continuous integration is a crucial practice in software development that involves testing your codebase, ensuring repository quality, reporting, and more, to maintain the health of your software project. This guide outlines how to set up a continuous integration workflow for your GitHub-based repositories.

## Setup

### Configure Tox test-automation

To streamline our test environment setup, we use `tox`, a powerful tool that automates testing across different environments. Begin by installing `tox`:

```bash
pip install tox
```

!!! Note
    [Tox](https://tox.wiki/en/4.9.0/) is a versatile tool that integrates comprehensive testing into your framework. Combined with a runner like GitHub Actions, it allows you to automate a wide range of tasks.

Configuring `tox` may involve some complexity. Start by defining what tests you want to run and what dependencies (such as packages or external services) are required for the tests. Organize these test tasks into logical steps.

!!! Warning "Missing"
    Refer to our comprehensive guide on configuring `tox` for detailed instructions.

!!! Info "Run test on multiple platforms"
    Our Tox environments are executed on all major platofrms including windows, linux and macos.

### Configure Continuous Integration using GitHub Actions

Our continuous integration (CI) process executes a series of tests, including running pytest and performing linting and code quality checks.

Here's an overview of the tasks involved:

- Running pytest
- Checking code syntax with `black`
- Verifying docstrings with `flake8`
- Sorting imports with `isort`

All these tools are executed as part of a job defined within a GitHub Actions workflow file. The workflow defines the tasks for a job, and a runner executes these tasks on a virtual machine provided by GitHub.

!!! Warning "Missing"
    To set up GitHub Actions workflows for your repository, follow our comprehensive guide.

Our CI workflow is triggered whenever there's a pull request or a commit to the `develop` or `production` branches. The workflow prepares the Python environment and installs relevant dependencies before executing the `tox` automation suite. If any errors are detected, the workflow fails and generates a detailed report for developers to review.

## Debugging

### Local Debugging

You can run your automation suite locally by typing the following command in your console. This is useful for verifying the outcome of your automation pipeline before pushing your code:

```bash
tox
```

Running this command will generate a comprehensive report, which may require some effort to debug.

### Remote Debugging on GitHub

For remote debugging, you can monitor the status of your automation jobs in two ways:

1. Create a pull request and view the CI status integration there.
2. Visit the [Actions tab of your repository](https://github.com/rl-institut/super-repo/actions) to see all available job executions.

These options allow you to closely monitor the progress and outcomes of your CI workflow, ensuring the reliability and quality of your codebase.

## Add new code test

To add a new test for any new functuionality you have added or you plan to add you should add a test. The test is imply added to the tests/ 
directory. 

See our examples ....