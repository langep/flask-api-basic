# flask-api-basic
This is a cookiecutte template to start out a simple flask api. It sets up:
Flask, pytest, pytest-cov, flake8, Sphinx and Docker.

## Requirements
 - [`cookiecutter`](https://github.com/audreyr/cookiecutter)

Install with pip:
```bash
pip install --user cookiecutter
```

For more information, refer to the official cookiecutter 
[documentation](https://cookiecutter.readthedocs.io/en/latest/readme.html).


## Setting up a project with this template

```bash
cookiecutter https://github.com/langep/flask-api-basic
```

Template variables:

  - `project_directory_name`: The command above will create a directory named like this.
    This should follow directory naming conventions.
  - `project_name`: Used as label for the project.
  - `project_short_description`: Used in README.md as description of the project.
  - `main_package_name`: Name of the main python package.
    This should follow python package naming conventions.
  - `author`: Your name.
  - `version`: Initial version of the project.

## Acknowledgment
Inspired by sloria's [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask).

