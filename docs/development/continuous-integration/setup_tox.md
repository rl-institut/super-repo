# Configure Tox test-automation

To streamline our test environment setup, we use `tox`, a powerful tool that
automates testing across different environments.

!!! Note
    [Tox](https://tox.wiki/en/stable/) is a powerful tool that simplifies
    and automates the process of testing Python projects across different environments.
    It ensures that your code is reliable, functional, and compatible with various
    Python versions and dependencies, ultimately leading to higher code quality
    and more robust software. Combined with a runner like GitHub Actions,
    it allows you to automate a wide range of tasks.

    ??? Info "Key features and functionalities"

        Tox creates isolated virtual environments for each specified Python version. This is crucial because different projects might have different dependencies or require specific Python versions. Isolation prevents conflicts between packages used by different projects.

        1. **Virtual Environments**: Tox creates isolated virtual environments for each specified Python version. This is crucial because different projects might have different dependencies or require specific Python versions. Isolation prevents conflicts between packages used by different projects.

        2. **Automated Testing**: Tox automates the entire testing process. It can be configured to run various types of tests, such as unit tests, integration tests, and even style checks. This ensures that the project is thoroughly tested in different environments without manual intervention.

        3. **Cross-Version and Cross-Platform Testing**: Tox enables you to test your code against multiple versions of Python, including Python 2 and Python 3. Additionally, it supports testing on various operating systems, allowing you to identify and address compatibility issues specific to different platforms.

        4. **Dependency Management**: Tox can help manage project dependencies by allowing you to specify different sets of dependencies for different testing environments. This helps ensure that your code works with different combinations of dependencies.

        5. **Configuration via tox.ini**: Tox uses a configuration file named `tox.ini` to define testing environments, dependencies, and testing commands. This file also allows you to set up various testing environments, customize test commands, and control other testing-related behaviors.

        6. **Consistency and Reproducibility**: Tox aids in maintaining consistency and reproducibility in your testing process. By setting up a standard testing workflow and environments, you reduce the risk of inconsistent results due to differences in developers' local setups.

        7. **Continuous Integration (CI) Integration**: Tox is often used in conjunction with CI systems like Jenkins, Travis CI, CircleCI, and GitHub Actions. By incorporating Tox into your CI pipeline, you can ensure that your code is automatically tested in multiple environments whenever changes are pushed to the repository.

        8. **Plugin System**: Tox has a plugin system that allows for extensibility. This means you can add custom functionality to the testing process, such as additional test runners, code analysis tools, and more.

## What is included in the tests?

Here's an overview of the testing-tasks involved:

- Running `pytest`
- Checking code syntax with `black`
- Verifying `docstrings` with `flake8`
- Sorting imports with `isort`

!!! Info "Run test on multiple platforms"
    Our Tox environments are executed on all major platforms including windows, linux and macos.

## Installation

Begin by installing [`tox`](https://tox.wiki/en/stable/installation.html):

```bash
pip install tox
```

!!! Note
    Setup and activate a [python environment](https://docs.python.org/3/library/venv.html) first.

## Setup

Configuring `tox` may involve some complexity.
Start by defining what tests you want to run and what dependencies
(such as packages or external services) are required for the tests.
Organize these test tasks into logical steps.

!!! Info "Tox User Guide"
    The official [tox User Guide](https://tox.wiki/en/stable/user_guide.html)
