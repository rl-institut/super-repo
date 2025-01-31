# Continuous Integration (CI) and Unit Tests

Continuous Integration (CI) ensures consistent code quality through automated
testing, reporting, and deployments.
The setup combines `GitHub Actions` and `tox` to streamline testing across
environments, making the process robust and efficient.

## GitHub Actions: Workflows

GitHub Actions automates key workflows like testing, linting, and code
quality checks. <br>
The CI pipeline includes the following tasks:  
- **Unit Testing**: Using `pytest` to ensure comprehensive test coverage
- **Code Formatting**: Validating syntax with `ruff`
- **Linting**: Verifying code style and docstrings with `ruff.lint`
- **Import Sorting**: Organizing imports with `ruff.lint.isort`

To set up workflows for the repository,
follow the [official GitHub guide](https://docs.github.com/en/actions/guides).<br>
The GitHub Actions are triggered on pull requests or commits to
selected branches.  
1. **Setup**: Prepares a Python environment and installs dependencies
2. **Testing**: Executes the `tox` automation suite to run the defined tests
3. **Reporting**: Generates detailed failure reports for debugging

GitHub Actions also automates documentation updates, ensuring the latest
changes from the `develop` branch are reflected. For more details, see
the [official GitHub Actions guide](https://docs.github.com/en/actions/guides).


## Tox: Automating Testing

[`tox`](https://tox.wiki/en/stable/) is a versatile tool for managing test
environments and automating testing tasks across Python versions and operating
systems (Linux, macOS, Windows). <br>
It enhances reproducibility and reliability by creating isolated environments
for testing:

- **Virtual Environments**: Isolates dependencies for each Python version
- **Automated Testing**: Runs tests and style checks (for example, `pytest`, `ruff`)
- **Cross-Platform Testing**: Ensures compatibility across versions and operating systems
- **Dependency Management**: Customizes dependencies for diverse test scenarios
- **Reproducibility**: Maintains consistent workflows by way of 📝`tox.ini`
- **Extensibility**: Supports plugins for custom functionality.

### Install

Install the required package in a python environment. <br>
   💻 `pip install tox` Install tox <br>
   💻 `tox` Run tox locally

## Adding and Managing Tests

New tests should be placed in the 📝`test` directory:  

- Add a test to validate new functionality
- Use `pytest` for unit tests, or extend 📝`tox.ini` for additional test configurations

By combining `tox` and GitHub Actions, our CI pipeline ensures robust,
reproducible, and scalable testing workflows.

### Test Patterns

1. **Unit and Integration Test**
   - **Purpose**: Test individual functions or methods.
   - **Framework**: `unittest`, `pytest`
   - **Example**: Simple function test and external API interactions.

2. **Functional Testing**
   - **Purpose**: Test complete functionality (end-to-end).
   - **Framework**: `pytest`, `selenium`
   - **Example**: Test user login in a web app.

3. **Mocking**
   - **Purpose**: Simulate external dependencies.
   - **Framework**: `unittest.mock`, `pytest-mock`
   - **Example**: Mock API calls in tests.

4. **Acceptance Testing**
   - **Purpose**: Verify the software meets requirements.
   - **Framework**: `pytest`, `Behave`
   - **Example**: Verify login form functionality.

5. **Performance Testing**
   - **Purpose**: Measure performance under load.
   - **Framework**: `pytest-benchmark`, `locust`
   - **Example**: Measure function execution time.

6. **Security Testing**
    - **Purpose**: Test for security vulnerabilities.
    - **Framework**: `bandit`
    - **Example**: Scan for hardcoded passwords.

7. **Snapshot Testing**
    - **Purpose**: Compare outputs to saved snapshots.
    - **Framework**: `pytest-snapshot`
    - **Example**: Compare function output snapshots.

8. **Property-Based Testing**
    - **Purpose**: Test properties of functions with random inputs.
    - **Framework**: `hypothesis`
    - **Example**: Test that a sorting function always returns a sorted list.

### Examples

The file 📝`test/test_example.py` contains basic examples for the functions in <br>
📝`super_repo/test_calculator.py`.

In Python, the `assert` statement is used to test if a condition is true. <br>
If the condition is false, an AssertionError is raised, indicating the test failed.

```python
result = add(3, 4)
assert result == 7
```

The `raises` context manager from the `pytest` library ensures that a ValueError is raised. <br>
The `match` argument specifies that the error message matches the expected error pattern.

```python
with raises(ValueError, match=r"Cannot divide by zero"):
    divide(15, 0)
```

We encourage contributions of additional tests and examples to help improve
coverage and showcase different use cases. Your input is valuable to enhancing the project!

!!! note "Used Icons"
    🐙 GitHub | 💠 git | 📝 File | 💻 Command Line
