# Install

## Environment (Conda)

With conda, you can create, export, list, remove, and update environments 
that have different versions of Python and/or packages installed in them. <br>
Switching or moving between environments is called activating the environment.
You can also share an environment file and import from `requirements.txt`.

💻 `conda env create -f environment.yml` Create conda environment <br>
💻 `activate py310` Activate environment <br>
💻 `python --version` Check python version


## Requirements

In Python the `requirements.txt` file helps manage dependencies. 
It's a text file that lists the packages that the Python project depends on.

💻 `pip install -r requirements.txt` Install from file


## Pyproject

This python package contains a `pyproject.toml` file that contains 
build system requirements and information, which are 
[used by pip](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) 
to build the package.
It contains the metadata of the software project.


!!! note "Used Icons"
    🐙 GitHub | 💠 git | 📝 File | 💻 Command Line
