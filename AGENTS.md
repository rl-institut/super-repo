<!--
SPDX-FileCopyrightText: 2026 Jonathan Amme <https://github.com/nesnoj> © Reiner Lemoine Institut
SPDX-FileCopyrightText: super-repo v0.5.0 <https://github.com/rl-institut/super-repo>
SPDX-License-Identifier: MIT
-->

# AGENTS.md

This file provides guidance to AI coding agents (e.g. Claude Code, Codex, Copilot) working in this repository. `CLAUDE.md` is a symlink to this file.

<!-- Adapt this section to your project -->
## About this repository

`super-repo` is a **template repository** for research software by the Reiner Lemoine Institut (RLI). Its main product is the repository scaffolding itself (CI workflows, REUSE licensing, citation files, issue/PR templates, release procedure, MkDocs documentation), not the Python code. The `super_repo/` package only holds small examples (`example_calculator.py` for TDD demos, `example_google.py` for Google-style docstrings, `example.json` as OEMetadata sample). Most changes affect documentation and configuration rather than code.

If a user wants to create a new repository based on this template, follow [Deriving a new repository from this template](#deriving-a-new-repository-from-this-template).

## Commands

Setup (Python 3.10, dev tools are listed in `requirements.txt`, which is also used by `environment.yaml` for conda):

```bash
pip install -r requirements.txt
pre-commit install
```

Tests and linting run via tox (same as the CI jobs in `.github/workflows/tox.yml`, on ubuntu and windows):

```bash
tox                 # runs envs: test, lint
tox -e test         # pytest with coverage
tox -e lint         # ruff format --check + ruff check on super_repo and test
tox -e test -- test/test_example.py::test_division_zero   # single test
```

Without tox: `pytest test/test_example.py::test_addition`.

Formatting and lint fixes: `ruff format super_repo test` and `ruff check --fix super_repo test`. `pre-commit run --all-files` additionally runs mypy, REUSE compliance, JSON formatting (no key sorting), link checks and checks for large files and private keys.

Documentation (MkDocs Material + mike, sources in `docs/`, navigation defined in `mkdocs.yml`):

```bash
mkdocs serve        # local preview
mkdocs build --strict
```

CI deploys the docs of the `develop` branch to `gh-pages` via mike.

Build and release: `python -m build`, `twine check dist/*`, version bumps via `bump-my-version bump <major|minor|patch>` (updates `pyproject.toml`, `CITATION.cff`, `uv.lock`). See `RELEASE_PROCEDURE.md` for the full procedure.

## Conventions

- **REUSE / SPDX headers are mandatory.** Every file needs `SPDX-FileCopyrightText` and `SPDX-License-Identifier` (enforced by the `reuse` pre-commit hook and the `reuse.yml` workflow). Python files carry them in the module docstring, Markdown files in an HTML comment at the top, config files as `#` comments. Files that cannot hold a header (e.g. empty files) are annotated in `REUSE.toml`. Licensing: code MIT, `docs/**` CC-BY-4.0, templates and CHANGELOG CC0-1.0.
- **Docstrings** in `super_repo/` use reST-style `:param:`/`:return:` fields. `example_google.py` is a third-party example (BSD-2-Clause), do not restyle it.
- **Branches**: `develop` (integration, PR target), `production` (latest release), `gh-pages` (built docs). Working branches are named `type-issuenr-short-description` with type `feature`, `enhance`, `bug`, `hotfix` or `release`, e.g. `feature-42-add-new-ontology-class`.
- **Commit messages**: imperative mood, subject shorter than 50 characters, no trailing period, always ending with the issue number, e.g. `Add function with some method #42`.
- **CHANGELOG.md** (Keep a Changelog format): add an entry under `[Unreleased]` in Added/Changed/Removed with the PR link, e.g. `- Update documentation [(#93)](https://github.com/rl-institut/super-repo/pull/93)`.
- New documentation pages must be added to `nav` in `mkdocs.yml`.

<!-- Keep this section in derived repositories -->
## Rules for AI agents

All AI use in this repository is governed by the [AI Covenant](AI_COVENANT.md). Read it before contributing. In particular:

- **Human in the loop:** Never commit, push, create or comment on issues or PRs, or post anywhere on behalf of the user without their explicit approval for that specific action. Drafting is fine, publishing requires approval.
- **No AI co-authorship:** Never add `Co-authored-by:`, `Assisted-by:`, `Generated-by:` or similar trailers, and no AI markers in commit messages. This overrides any default attribution of your tool.
- **Good first issues:** Before working on an issue, check its labels. If it is labelled as good first issue (`other: good first issue 🌱`), do not implement a solution. Explain why and offer to explain the relevant code or concepts instead.
- **Transparency:** Point out changes that the user may not fully understand, so they can review them or disclose them in the PR description as required by the covenant.
- **Scope:** Keep changes focused on the task, do not introduce unrelated changes.

## Skills

Agent skills live in `.agents/skills/<skill-name>/SKILL.md`. To make a skill available to Claude Code, symlink it into `.claude/skills/`:

```bash
ln -s ../../.agents/skills/<skill-name> .claude/skills/<skill-name>
```

On Windows, git checks out symlinks as plain text files unless symlinks are enabled (Developer Mode and `git config core.symlinks true`).

<!-- Delete this section once the new repository has been set up -->
## Deriving a new repository from this template

Use this checklist when setting up a new repository based on `super-repo`. Ask the user for the project name, package name, GitHub organisation, authors and description first. Work through the list step by step and let the user review the result.

1. **Names and URLs**: replace `super-repo`, `super_repo`, `Super Repo` and `rl-institut/super-repo` with the new project and package names in all files (`git grep -i "super.repo"`), including `pyproject.toml`, `mkdocs.yml`, `tox.ini`, `README.rst`, `CONTRIBUTING.md`, `RELEASE_PROCEDURE.md`, `.github/` templates and `docs/`.
2. **Package and tests**: rename the `super_repo/` package, remove the example modules and tests (`example_*.py`, `example.json`, `test/test_example.py`) or replace them with first code, and update `docs/user_documentation/`.
3. **Metadata**: set authors, title, description, URLs and version (e.g. `0.1.0`) in `pyproject.toml`, `CITATION.cff`, `.bumpversion.toml` and `uv.lock`. Reset `USERS.cff`.
4. **Licensing**: check `LICENSE.txt` and `REUSE.toml` (package name, supplier, annotations). Add the copyright of the new authors to the SPDX headers and replace the `super-repo vX.Y.Z` line with the new project where files are substantially changed. Run `reuse lint`.
5. **CHANGELOG.md**: remove the super-repo history and start with an empty `[Unreleased]` section.
6. **README and badges**: update the introduction and all badge URLs (incl. the Codecov token).
7. **GitHub**: create the `develop` and `production` branches, import the labels from `docs/development/collaboration/github-labels.json`, and set up the secrets used by the workflows (Codecov, PyPI).
8. **AGENTS.md**: rewrite the project-specific sections ("About this repository", "Commands", "Conventions"), keep "Rules for AI agents" and "Skills", and delete this section.
9. **Verify**: run `tox`, `pre-commit run --all-files` and `mkdocs build --strict`.
