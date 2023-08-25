# Code Style

This document aims to provide clear instructions on how to write clean,
readable, and maintainable Python code.
Adhering to these guidelines will ensure consistency across the codebase and
foster collaboration among contributors.
Maintaining a consistent code style is crucial for the readability and
maintainability of a Python project.

We enforce most of the following guidelines in our
[Continuous-Integration pipeline](../../development/continuous-integration/index.md)
that check the code automatically.

## 1. Installation

Before contributing to the project, make sure you have the necessary tools
installed for code style enforcement.
We utilize [pre-commit](https://github.com/pre-commit/pre-commit-hooks)
to automate code checks before committing changes.
To install and setup pre-commit, see [Continuous-Integration pipeline](../../development/git/#pre-commit)

## 2. Code Formatting

Consistent code formatting enhances readability and reduces unnecessary
debates about style.
We use [Black](https://github.com/psf/black) as our Python code formatter.
It automatically formats your code to adhere to the project's style guidelines.

## 3. Naming Conventions

While we don't enforce strict naming conventions, we encourage compliance with
[PEP8](https://www.python.org/dev/peps/pep-0008/) and the
[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
for consistency. Descriptive names and adherence to conventions improve code clarity.

## 4. Indentation and Whitespace

We follow the Python standard of using 4 spaces for tab indentation.
Do not include any trailing whitespace at the end of lines.

## 5. Comments and Documentation

Effective comments and docstrings are vital for code understanding.
Use comments to explain complex logic and docstrings to describe functions,
classes, and modules.
Following good documentation practices ensures code is understandable to others.

## 6. Imports

Our imports are automatically checked and sorted using
[isort](https://github.com/pycqa/isort).
This tool organizes imports based on the Black code style and optimizes import
statements for readability.

## 7. Code Structure and Organization

Maintain a logical structure within files, grouping related functions and
classes. Consider the readability of your code and strive for modular,
well-organized files.
