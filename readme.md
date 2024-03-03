# A python module template

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a typical Python library following modern packaging conventions.

It utilizes popular libraries to fully automate all development and deployment tasks.

## About this project

In 2019, I worked on [template-python](https://github.com/geronimo-iia/template-python) which was based on [Jace's Python Template](https://github.com/jacebrowning/template-python).
For me, the goal was to be able to start quickly a new python project with all basics stuff ever configured, like :

- project definition using pytoml
- all lint tools (isort, black, ...)
- test unit ready to feed
- a basic documentation (about, api, etc...)
- a poetry command line utility (I'm not a big fan of long command line when i develop...)

In 2021, after two years of usage (for personal and work use), it was time to simplify all those things that we did not like: all little stich and glues around a project.

- We did not use [precommit](https://pre-commit.com/) anymore, ... Most often, our dev teams by-pass the pre-commit (nasty evils), so we let our ci doing his job (aka KillThemAll target).
- All tooling are configured using `pyproject.toml`, we wanna avoid the mess of configuration files...

In 2023, 4 year ever, python is always my favorite language (even if I start working around rust ...). It's time to another update:

- Documentation is always/often a painfull point. I had used a lot Sphinx, really like it, but mkdocs just do my things in a very simple way. So let's choose this way.
- flakehell could be replaced by ruff. Less configuration, and quicker so...
- add github action for check current change on build
- automate github release, publish on pypi, site documentation on a tag.

In 2024, we still use a lot of command into `makefile`, dependencies can be managed with dependabot on github, so in this flavour :

- Replace makefile with [Poe the Poet](https://poethepoet.natn.io/index.html) as a poetry plugin
- add dependabot configuration to manage developement and production dependencies update.
- use dependencies group declaration:
  - `dev` group for all dev tools
  - `docs` group which can be installed with `poetry install --with docs`
- add option for package mode: set it to false when you want to use Poetry only for dependency management but not for packaging.

## Features

* Core:
  * [poetry](https://python-poetry.org/) to rules them all
  * [pep-0518](https://www.python.org/dev/peps/pep-0518/) alias `pyproject.toml` for managing dependencies, package metadata, ...
* Project tooling:
  * Setup formatting with [isort](https://github.com/PyCQA/isort) and [black](https://github.com/psf/black)
  * Analysing with [ruff](https://github.com/charliermarsh/ruff)
  * Type checking with `mypy`
  * Running tests with `pytest`
  * [Poe the Poet](https://poethepoet.natn.io/index.html) for automating common development tasks
* Preconfigured setup for:
  * [Github workflow](https://guides.github.com/introduction/flow/):
    * 'package': launch an install/test/check on each push and pull request on 'main' branch.
    * 'release": on each tag push, launch:
      - a github release 
      - a pypi publish . You have to configure a secret 'PYPI_TOKEN' in your git repository.
      - a site documentation publication
  * [dependabot](https://github.com/dependabot) to manage dependencies updates.
* Documentation:
  * Docstring styling with `pydocstyle`
  * Building documentation with `mkdocs`
  * Auto generation of API reference
  * Expose with documentation site under 'gh-pages' branch per default.


## Usage

Install `cookiecutter` and generate a project:

```
$ pip install cookiecutter
$ cookiecutter gh:geronimo-iia/python-module-template -f
```

Cookiecutter will ask you for some basic info (your name, project name, python package name, etc.) and generate a base Python project for you.

Poe target list:

| Name                    | Comment                                                                                  |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| poetry poe check        | Run linters and static analysis                                                          |
| poetry poe test         | Run unit tests                                                                           |
| poetry poe build        | Builds the source and wheels archives (and run check & test target)                      |
| poetry poe publish      | Publishes the package, previously built with the build command, to the remote repository |
| poetry poe docs         | Builds  site documentation.                                                              |
| poetry poe docs-publish | Build and publish site documentation.                                                    |
| poetry poe clean        | Delete all generated and temporary files                                                 |
| poetry poe requirements | Generate requirements.txt                                                                |
|                         |                                                                                          |

You could retrieve those commands with `poetry poe`. It will output something like this :

```
Poe the Poet - A task runner that works well with poetry.
version 0.25.0

Result: No task specified.

USAGE
  poetry poe [-h] [-v | -q] [--root PATH] [--ansi | --no-ansi] task [task arguments]

GLOBAL OPTIONS
  -h, --help     Show this help page and exit
  --version      Print the version and exit
  -v, --verbose  Increase command output (repeatable)
  -q, --quiet    Decrease command output (repeatable)
  -d, --dry-run  Print the task contents but don't actually run it
  --root PATH    Specify where to find the pyproject.toml
  --ansi         Force enable ANSI output
  --no-ansi      Force disable ANSI output

CONFIGURED TASKS
  build          Build module
  publish        Publish module
  check          Run Linter
  test           Run unit tests
  docs           Build site documentation
  docs-publish   Publish site documentation
  clean          Remove all generated and temporary files
  requirements   Generate requirements.txt
```


Make Target list:

| Name                    | Comment                                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------------------- |
| make install            | Install project dependencies                                                                    |
| make configure          | Configure poetry                                                                                |
| make tag                | Create and push a tag based on current project version. This will launch github release action. |
| make next-patch-version | Increment patch version of the project.                                                         |
|                         |                                                                                                 |

## Note on configuration of Poetry

To configure poetry, you could use `make configure`or run :

```bash
# virtualenvs under project folder
poetry config virtualenvs.in-project true

# install needed plugins
poetry self add poetry-plugin-export
poetry self add 'poethepoet[poetry_plugin]'

# update tooling
poetry run python -m pip install --upgrade pip
poetry run python -m pip install --upgrade setuptools
```

See also:

- https://python-poetry.org/docs/#installation
- https://poethepoet.natn.io/installation.html

