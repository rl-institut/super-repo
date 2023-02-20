# Documentation

- README.rst
- CHANGELOG.md
- docs/
- MkDocs
- mkdocstrings


## MkDocs

### Install
Install the required packages. <br>
`pip install mkdocs` install MkDocs <br>
`pip install mkdocs-material` install the material theme

### Build
Generate the documentation. <br>
`mkdocs serve` start the local live version of the documentation <br>
`mkdocs build` create a folder `site` with the documentation

### Publish

#### Manually
Publish documentation on **GitHub Pages**. <br>
`mkdocs gh-deploy` manually deploys the documentation files

#### GitHub Action
Deploy the documentation with **GitHub Actions**. <br>
The file `.github\workflows\gh-pages.yml` creates an automated GitHub workflow. <br>
It is configured to be pushed to the branch `gh-page` and then deployed online. <br>
A commit on the `production` branch triggers the workflow. 
