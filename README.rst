..
  SPDX-FileCopyrightText: 2022 Ludwig Hülk <https://github.com/Ludee> © Reiner Lemoine Institut
  SPDX-FileCopyrightText: super-repo v0.5.0 <https://github.com/rl-institut/super-repo>
  SPDX-License-Identifier: MIT

.. figure:: https://user-images.githubusercontent.com/14353512/185425447-85dbcde9-f3a2-4f06-a2db-0dee43af2f5f.png
    :align: left
    :target: https://github.com/rl-institut/super-repo/
    :alt: Repo logo

==========
super-repo
==========

**A template repo to test and document elements and features for research software.**

.. list-table::
   :widths: auto

   * - License
     - |badge_license| |badge_reuse|
   * - Documentation
     - |badge_documentation| |badge_mkdocs|
   * - Tests
     - |badge_tox| |badge_codecov|
   * - Publication
     - |badge_pypi| |badge_python| |badge_pypi_downloads|
   * - Development
     - |badge_issue_open| |badge_issue_closes| |badge_pr_open| |badge_pr_closes|
   * - Community
     - |badge_contributions| |badge_contributors| |badge_repo_counts| |badge_matrix|

.. contents::
    :depth: 2
    :local:
    :backlinks: top

Introduction
============
| A template repo to test and document elements and features for research software.
| It implements the collection of repository elements collected in this `Etherpad <https://etherpad.wikimedia.org/p/super-repo>`_.
| The goal is to simplify and standardize the creation of software in GitHub repositories.

Documentation
=============
| The documentation is created with Markdown using `MkDocs <https://www.mkdocs.org/>`_ and `mike <https://github.com/jimporter/mike>`_.
| All files are stored in the ``docs`` folder of the repository.
| A **GitHub Actions** deploys the ``develop`` branch on a **GitHub Page**.
| The documentation page is: `rl-institut.github.io/super-repo/ <https://rl-institut.github.io/super-repo/>`_

Collaboration
=============
| Everyone is invited to develop this repository with good intentions.
| Please follow the workflow described in the `CONTRIBUTING.md <https://github.com/rl-institut/super-repo/blob/production/CONTRIBUTING.md>`_.

Contributors:

.. figure:: https://contrib.rocks/image?repo=rl-institut/super-repo
    :align: left
    :target: https://github.com/rl-institut/super-repo/graphs/contributors
    :alt: [contrib.rocks](https://contrib.rocks)

License and Citation
====================
| The code of this repository is licensed under the **MIT License** (MIT).
| See `LICENSE.txt <https://github.com/rl-institut/super-repo/blob/production/LICENSE.txt>`_ for rights and obligations.
| See the *Cite this repository* function or `CITATION.cff <https://github.com/rl-institut/super-repo/blob/production/CITATION.cff>`_ for citation of this repository.
| Copyright: `super-repo <https://github.com/rl-institut/super-repo/>`_ © `Reiner Lemoine Institut <https://reiner-lemoine-institut.de/>`_ | `MIT <LICENSE.txt>`_


.. |badge_license| image:: https://img.shields.io/github/license/rl-institut/super-repo
    :target: https://github.com/rl-institut/super-repo/blob/production/LICENSE.txt
    :alt: License

.. |badge_reuse| image:: https://api.reuse.software/badge/github.com/rl-institut/super-repo
    :target: https://api.reuse.software/info/github.com/rl-institut/super-repo
    :alt: REUSE

.. |badge_documentation| image:: https://img.shields.io/github/actions/workflow/status/rl-institut/super-repo/documentation.yml?branch=develop&label=documentation
    :target: https://rl-institut.github.io/super-repo/
    :alt: Documentation

.. |badge_mkdocs| image:: https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=for-the-badge&logo=MaterialForMkDocs&logoColor=white
    :target: https://squidfunk.github.io/mkdocs-material/
    :alt: MkDocs

.. |badge_tox| image:: https://img.shields.io/github/actions/workflow/status/rl-institut/super-repo/tox.yml?label=tox
    :target: https://github.com/rl-institut/super-repo/actions/workflows/tox.yml
    :alt: Tox Tests

.. |badge_codecov| image:: https://codecov.io/gh/rl-institut/super-repo/graph/badge.svg?token=YYCJI3D5G5
    :target: https://codecov.io/gh/rl-institut/super-repo
    :alt: Codecov

.. |badge_pypi| image:: https://img.shields.io/pypi/v/super-repo
    :target: https://pypi.org/project/super-repo/
    :alt: PyPI Version

.. |badge_python| image:: https://img.shields.io/pypi/pyversions/super-repo
    :target: https://github.com/rl-institut/super-repo/blob/develop/pyproject.toml
    :alt: PyPI Python Version

.. |badge_pypi_downloads| image:: https://img.shields.io/pypi/dm/super-repo
    :target: https://pypi.org/project/super-repo/
    :alt: PyPI Downloads

.. |badge_issue_open| image:: https://img.shields.io/github/issues-raw/rl-institut/super-repo
    :target: https://github.com/rl-institut/super-repo/issues
    :alt: open issues

.. |badge_issue_closes| image:: https://img.shields.io/github/issues-closed-raw/rl-institut/super-repo
    :target: https://github.com/rl-institut/super-repo/issues?q=is%3Aissue+is%3Aclosed
    :alt: closes issues

.. |badge_pr_open| image:: https://img.shields.io/github/issues-pr-raw/rl-institut/super-repo
    :target: https://github.com/rl-institut/super-repo/pulls
    :alt: closes issues

.. |badge_pr_closes| image:: https://img.shields.io/github/issues-pr-closed-raw/rl-institut/super-repo
    :target: https://github.com/rl-institut/super-repo/pulls?q=is%3Apr+is%3Aclosed
    :alt: closes issues

.. |badge_contributions| image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
    :target: https://github.com/rl-institut/super-repo/blob/production/CONTRIBUTING.md
    :alt: contributions

.. |badge_contributors| image:: https://img.shields.io/github/contributors/rl-institut/super-repo
    :target: https://github.com/rl-institut/super-repo/graphs/contributors
    :alt: contributors

.. |badge_repo_counts| image:: https://hits.sh/github.com/rl-institut/super-repo.svg
    :target: https://hits.sh/github.com/rl-institut/super-repo/
    :alt: hits

.. |badge_matrix| image:: https://img.shields.io/matrix/super-repo:matrix.org
    :target: https://app.element.io/#/room/#super-repo:matrix.org
    :alt: Matrix
