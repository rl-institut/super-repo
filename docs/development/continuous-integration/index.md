# Continuous Integration

Continuous Integration (CI) is a good practice in software development that
involves automated testing of code, ensuring repository quality, reporting, and
automate deployments. <br>
The process involves the utilization of multiple technologies.
Once the setup is complete, it's possible to create new test and
also to interpret the output of success or error messages as response from the
test-execution. A brief summary of this process is also provided for reference.

## Automation

The package [tox](https://github.com/tox-dev/tox) automates the process of testing
Python projects. It provides support for creating and managing test environments
across cross different environments, Python versions, and dependencies. <br>
It ensures that the code is reliable, functional, and compatible on different
computers leading to higher code quality and more robust software.
Combined with GitHub Actions, it allows you to automate a wide range of tasks.

### Key features and functionalities

For each specified Python version, tox creates isolated virtual environments.
This is important because different projects might have different dependencies
or require specific Python versions and run on different platforms like Windows, Linux, or MacOS.
Isolation prevents conflicts between packages used by different projects.

1. **Virtual Environments**: Tox creates isolated virtual environments for each specified Python version. This is crucial because different projects might have different dependencies or require specific Python versions. Isolation prevents conflicts between packages used by different projects.
2. **Automated Testing**: Tox automates the entire testing process. It can be configured to run various types of tests, such as unit tests, integration tests, and even style checks. This ensures that the project is thoroughly tested in different environments without manual intervention.
3. **Cross-Version and Cross-Platform Testing**: Tox enables you to test your code against multiple versions of Python, including Python 2 and Python 3. Additionally, it supports testing on various operating systems, allowing you to identify and address compatibility issues specific to different platforms.
4. **Dependency Management**: Tox can help manage project dependencies by allowing you to specify different sets of dependencies for different testing environments. This helps ensure that your code works with different combinations of dependencies.
5. **Configuration via tox.ini**: Tox uses a configuration file named `tox.ini` to define testing environments, dependencies, and testing commands. This file also allows you to set up various testing environments, customize test commands, and control other testing-related behaviors.
6. **Consistency and Reproducibility**: Tox aids in maintaining consistency and reproducibility in your testing process. By setting up a standard testing workflow and environments, you reduce the risk of inconsistent results due to differences in developers' local setups.
7. **Continuous Integration (CI)**: Tox is often used in conjunction with CI systems like Jenkins, Travis CI, CircleCI, and GitHub Actions. By incorporating Tox into your CI pipeline, you can ensure that your code is automatically tested in multiple environments whenever changes are pushed to the repository.
8. **Plugin System**: Tox has a plugin system that allows for extensibility. This means you can add custom functionality to the testing process, such as additional test runners, code analysis tools, and more.

## Install

Install the required package [`tox`](https://tox.wiki/en/stable/installation.html) in a python environment. <br>
💻 `pip install tox` install tox <br>

## Setup

Configuring `tox` may involve some complexity. <br>
See the official [tox user guide](https://tox.wiki/en/stable/user_guide.html) for further information.

All test stages are setup in the configuration file `tox.ini`.
This file configures all test environments as well as the tools and configuration
used to run tests and checks.

## Testing

### pytest

For smaller projects or a more straightforward approach,
testing can also be effectively accomplished using [pytest](https://github.com/pytest-dev/pytest/).
This allows for efficient testing without the additional complexity of setting
up and managing multiple environments.

### black

Checking code syntax with `black`

### flake8

Verifying `docstrings` with `flake8`

### isort

Sorting imports with `isort`

### Django tests

Testing Django projects with [Django tests](https://docs.djangoproject.com/en/3.2/topics/testing/).

## GitHub Actions

GitHub offers an integrated CI called `GitHub Actions`,
which enables the definition of test workflows and events.
These workflows can be executed, for instance,
with every pull request or new commit on a specific branch.
To set up workflows for your repository, follow the [Guides for GitHub Actions](https://docs.github.com/en/actions/guides).

### Automated Testing

All tests are defined within the workflow file `.github/workflows/automated-testing.yml`.
The workflow defines the tasks for a action, and a runner executes these tasks on a
virtual machine provided by GitHub.

The workflow is triggered whenever there's a pull request or a commit to the `develop` or `production` branches.
The workflow prepares the Python environment and installs relevant dependencies before executing the `tox` automation suite.
If any errors are detected, the workflow fails and generates a detailed report for developers to review.

### Building and deploying the documentation

Another use case that involves the GitHub-Actions is the automated deployment of the documentation.
While all minor versions are manually deployed using [mike](https://rl-institut.github.io/super-repo/latest/development/documentation/#mike).
GitHub-Actions workflow builds and deploys the `develop` branch.
This ensures that the documentation is automatically updated if a new feature or update is available.
