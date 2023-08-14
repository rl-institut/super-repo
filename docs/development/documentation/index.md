# Documentation

## README
The repository contains a `README.rst` file with basic information. <br>
It gives a short introduction to the project and links to other relevant files.

## Changelog
The `CHANGELOG.md` is a record of all notable changes made to a project. <br>
It is structured by each release and divided by additions, changes, and removals. <br>

## MkDocs
[MkDocs](https://www.mkdocs.org/) is a fast and simple static site generator that is used for documentation. <br>
The source files are written in [Markdown](https://www.markdownguide.org/cheat-sheet/), and configured with `mkdocs.yml`. <br>
[Material theme](https://squidfunk.github.io/mkdocs-material/) enables 
additional features and an elegant design. <br>

### Install
Install the required packages in a python environment. <br>
💻 `pip install mkdocs` install MkDocs <br>
💻 `pip install mkdocs-material` install the material theme

### Build
Generate the documentation locally. <br>
💻 `mkdocs serve` start the local live version of the documentation <br>
💻 `mkdocs build` create a folder `site` with the documentation

### Publish

#### Manually
Publish documentation on **GitHub Pages**. <br>
💻 `mkdocs gh-deploy` manually deploys the documentation files

#### GitHub Action (deprecated)
🐙 Deploy the documentation with **GitHub Actions**. <br>
The file `.github\workflows\gh-pages.yml` creates an automated GitHub workflow. <br>
It is configured to be pushed to the branch `gh-page` and then deployed online. <br>
A commit on the `production` branch triggers the workflow. 

!!! warning "Using mike with GitHub Actions"
    This feature is not compatible with the versioning of the documentation with `mike`! <br>
    The action overrides all manually deployed versions. <br>
    🐙 To disable an existing `GitHub Action`, follow [these instructions](https://docs.github.com/de/enterprise-cloud@latest/actions/using-workflows/disabling-and-enabling-a-workflow).

### Mike
The package [mike](https://github.com/jimporter/mike) is used to deploy [multiple versions](https://squidfunk.github.io/mkdocs-material/setup/setting-up-versioning/?h=versioning) of the documentation.<br>
💻 `pip install mike` install mike <br>
💻 `mike deploy --push --update-aliases 0.1 latest` deploys the latest version <br>
💻 `mike set-default --push latest` Set the default version to latest

!!! note "Mike Versions"
    It is recommended to use only the **Minor Versions** (e.g. 0.1) and exclude the **Patch Version** (e.g. 0.1.1)!

Other useful commands are: <br>
💻 `mike serve` test mike on [`http://localhost:8000`](http://localhost:8000) <br>
💻 `mike list` list all versions <br>
💻 `mike retitle 1.0.0 1.0.1 --push` rename a version <br>
💻 `mike delete 0.1 --push` deletes a specific versions <br>
💻 `mike delete --all --push` deletes all versions

When adding older versions, load the `Git Tags` used for the releases: <br>
💠 `git checkout v0.1.1` <br>
💻 `mike deploy --push --update-aliases 0.1 latest` deploys the old version

When building mike locally, the branch `gh-pages` is modified locally. <br>
💻 `error: gh-pages is unrelated to origin/gh-pages` <br>
💠 `git branch -D gh-pages` delete the local documentation branch

## mkdocstrings
[mkdocstrings](https://mkdocstrings.github.io/) generates automatic 
documentation (autodocs) from [Google style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). <br>
💻 `pip install mkdocstrings` install mkdocstrings


!!! note "Used Icons"
    🐙 GitHub | 💠 git | 📝 File | 💻 Command Line
