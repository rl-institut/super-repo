# Release

The software release has four main goals:

1. Merge the new features to the `production` branch
2. Create a [GitHub Release](https://github.com/rl-institut/super-repository/releases)
3. Update the documentation
4. Publish a new version of the package at PyPI

The [RELEASE_PROCEDURE.md](https://github.com/rl-institut/super-repository/blob/production/RELEASE_PROCEDURE.md)
contain detailed instructions to do a release.

## Automated Versioning with Bumpversion

**Bumpversion** is a tool for automated version management in software projects. <br>
It ensures consistent version updates across files and documentation. <br>
By specifying a part to increment (major, minor, or patch), Bumpversion updates
the version number and creates a Git commit or tag automatically.
This streamlines release workflows, reduces human error, and keeps project versioning synchronized.  

Install package:  
💻 `pip install --upgrade bumpversion`

For configuration, create a `.bumpversion.toml` file to specify versioning rules and affected files.

Use bumpversion:  
💻 `bumpversion --current-version 0.2.0 minor`
