# Continuous Integration with GitHub

Continuous integration (CI) is a crucial practice in software development that involves testing your codebase, ensuring repository quality, reporting, automate deployments and more, to maintain the health of your software project. This guide outlines how to set up a continuous integration workflow for your GitHub-based repositories. The process involves the utilization of multiple technologies. Once the setup is complete, it's essential to be able to create new test and also to interpret the output of success or error messages as response from the test-execution. A brief summary of this process is also provided here for your reference.

## Introduction

!!! Warning
    Missing
### Testing the codebase & ensuring code quality

In our projects, we utilize [`Tox`](https://tox.wiki/en/stable/) together with [`pytest`](https://docs.pytest.org/en/stable/) or [Django tests](https://docs.djangoproject.com/en/3.2/topics/testing/). In addition to configuring the testing software and crafting tests, we leverage GitHub's services. GitHub offers an integrated CI tool called Actions, which enables the definition of test workflows and events. These workflows can be executed, for instance, with every pull request or new commit on a specific branch. Follow the upcoming steps and instructions to navigate through the setup of the employed technologies.

!!! Info
    Tox proves to be a powerful tool, providing comprehensive support for creating and managing test environments across various Python versions and dependencies. However, for smaller projects or those seeking a more straightforward approach, testing can also be effectively accomplished using `pytest` alone. This allows for efficient testing without the additional complexity of setting up and managing multiple environments through Tox. Choose the approach that best suits your project's requirements and size, ensuring an optimal testing experience.

### Building and deploying the documentation

Another use case that involves the GitHub-Actions is the automated deployment. By adding another GitHub service called Pages to the stack we can define a GitHub-Actions workflow that automatically builds&deploys our `mkdocs` based documentation. This ensures that our documentation is automatically updated if a new release or new commit is available.

!!! Warning
    Link to `mkdocs` hosted on GH-Pages guide.

## Setup

We have to configure a runner that can listen for events that trigger test runs and also provides the infrastructure to execute the test automatically. GitHub-Actions provides us a hosted runner that we can use and configure using a configuration file like `.github/workflows/automated-testing.yml`.

- [More information on how to setup GitHub-Action](setup_github_actions.md)

To setup testing we also have to configure the automated test runs that are executed automatically via GitHub-Action. As we want to use `tox` we can setup all test stages in a single configuration file that is named `tox.ini`. This file configures all test environments as well as the tools and tool-configuration that we use to run tests and other code-quality checks.

- [More information on how to setup `tox`](setup_tox.md)
