# Git

## Branches

[Git Branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)
are used to structure the developments and improvements.

### Permanent Branches

- **production** - includes the current stable (latest) version
- **develop** - includes all current developments

### Temporary Branches

- **feature** - includes the feature and improvements that will be implemented
- **hotfix** - includes small improvements before a release, should be branched from a release branch
- **release** - includes the current version to be released

The majority of the development will be done in `feature` branches.

## Gitignore

This file specifies intentionally untracked files to ignore.
It is copied from [a collection of .gitignore templates](https://github.com/github/gitignore). <br>
For more information about how `.gitignore` files work, see the [Ignoring Files chapter](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring) of the Pro Git book.

## Issue Templates

[Issue Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)
offer specific functions and default configurations for new issues.

- [Feature Issue](https://github.com/rl-institut/super-repo/blob/production/.github/ISSUE_TEMPLATE/issue_template_feature.md)
- [Bug Issue](https://github.com/rl-institut/super-repo/blob/production/.github/ISSUE_TEMPLATE/issue_template_bug.md)
- [Release Issue](https://github.com/rl-institut/super-repo/blob/production/.github/ISSUE_TEMPLATE/issue_template_release.md)
- [User Kudos Issue](https://github.com/rl-institut/super-repo/blob/production/.github/ISSUE_TEMPLATE/issue_template_user_kudos.md)

## Pull Request (PR) Template

The [Pull Request Template](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
is used for all PR, because it is only possible to create a single one.
It includes all needed information to merge branches and release new versions.

## GitHub Labels

GitHub Labels are used to organize Issues and PR. <br>
Colours and emoticons improve presentation.

Categories:
- **type**:
    - bug :bug: "Something isn't working" [default] #FEF1C7
    - feature :hammer_and_wrench: "New feature or request" #FEF1C7
    - enhancement :gear: "Improvement of an existing feature" [default] #FEF1C7
    - question :question: "Further information is requested" [default] #FEF1C7
    - release :rocket: "Release procedure" #FEF1C7
- **part**:
    - backend :bricks: "Backend component" #A7F3D5
    - frontend :desktop_computer: "Improvement of design or content" #A7F3D5
    - docu :book: "Improvements or additions to documentation" [default] #A7F3D5
    - github :octocat: "Improvement of the organisation or repo" #A7F3D5
    - community :earth_africa: "Concerns the community" #A7F3D5
- **status**:
    - active :construction: "Work in progress" #93C5FD
    - discussion :speech_balloon: "Discussion is ongoing" #93C5FD
    - blocked :stop_sign: "Blocked or impeded progress" #F9A8D4v
    - decision wanted :ballot_box: "Decision is needed" #F9A8D4
    - completed :heavy_check_mark: "Task has been completed" #6EE7B7
- **priority**:
    - low :sloth: "Low priority" #FCD34D
    - high :zap: "High priority" #FDBA74
    - critical :fire: "Critical priority" #FCA5A5
- resolution:
    - released :tada: "Resolved and released" #ECDCF8
    - wontfix :no_entry: "This will not be worked on" [default] #ECDCF8
    - invalid :x: "Issue is invalid" [default] #ECDCF8
    - duplicate :feet: "This issue or pull request already exists" [default] #ECDCF8
- other:
    - good first issue :seedling: "Good for newcomers" [default] #EBF0F3
    - help wanted :raising_hand: "Help or assistance is needed" [default] #EBF0F3
    - example :triangular_ruler: "Provides an example" #EBF0F3

## GitHub Workflows (Actions)

[GitHub Actions](https://github.com/rl-institut/super-repo/actions)
are used to automate processes of the repository. <br>
Main use-cases are building and publishing the documentation and run automated tests.

## Pre-commit

**Pre-commit** is a tool to easily setup and run `pre-commit hooks` for your git repository.<br>
See the documentation of [pre-commit](https://pre-commit.com/) for further information.<br>
It is used to improve auto-format code, do linting and run tests before every commit.

### Install

Install the required package in a python environment. <br>
💻 `pip install pre-commit` install pre-commit <br>
💻 `pre-commit install` install pre-commit

### Setup

The hooks are configured in the `.pre-commit-config.yaml` file.<br>
List of implemented hooks:

- [Pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) - Out-of-the-box hooks
- [Black](https://github.com/psf/black) - Python code formatter
- [isort](https://github.com/pycqa/isort) - Sort Python imports
- [Ruff](https://github.com/astral-sh/ruff-pre-commit) - Fast Python linter, written in Rust
- [Flake8](https://github.com/pycqa/flake8) - Python linter with PyFlakes and pycodestyle
- [mypy mirror](https://github.com/pre-commit/mirrors-mypy) - Added static types to Python
- [mirrors-prettier](https://github.com/pre-commit/mirrors-prettier) - Formatting for other files then python scripts
- [reuse](https://github.com/fsfe/reuse-tool) - License and copyright information

### Use

All commits will trigger the hooks automatically.<br>
💠 `git commit file -m "Commit message #IssueNr"` to commit

Commit without running the hooks.<br>
💠 `git commit --no-verify file` to commit without hooks

!!! note "Line endings"
    There can be problems with file line endings on Windows, `CRLF` is used on Windows and `LF` is used on Linux.

To run the hooks on all files in your repository use:<br>
💻 `pre-commit run --all-files`

!!! warning "Markdown files / Admonitions"
    If the hook is applied to markdown files that include special formatting,
    (e.g. `mkdocs.yml`), this can introduce incorrect changes. <br>
    This effects [admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) boxes for MkDocs.
