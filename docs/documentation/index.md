# Documentation

- README.rst
- CHANGELOG.md
- docs/
- MkDocs
- mkdocstrings


## MkDocs

### Install
`pip install mkdocs` install MkDocs <br>
`pip install mkdocs-material` install the material theme <br>

### Build
`mkdocs serve` start the local live version of the documentation

`mkdocs build` build the documentation

### Publish
Publish MkDocs project on **GitHub Pages** (requires permissions on repository) <br>
`mkdocs gh-deploy` manually deploy the local docs files to github pages

Deploy with **GitHub Actions** 
The file `.github\workflows\gh-pages.yml` creates an automated GitHub workflow.
It is configured that it is pushed to the branch `gh-page` and then deployed online.
A commit on the `production` branch triggers the workflow. 
