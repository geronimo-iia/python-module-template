# A python module template

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a typical Python library following modern packaging conventions.

It utilizes popular libraries to fully automate all development and deployment tasks.


## Features

* Core:
  * [uv](https://docs.astral.sh/uv/) as depdencies manager
  * [pep-0518](https://www.python.org/dev/peps/pep-0518/) alias `pyproject.toml` for managing dependencies, package metadata, ...
* Project tooling:
  * Formatting, Analysing with [ruff](https://github.com/charliermarsh/ruff)
  * Type checking with `pyright`
  * Running tests with `pytest`
  * [Poe the Poet](https://poethepoet.natn.io/index.html) for automating common development tasks
* Preconfigured setup for:
  * [Github workflow](https://guides.github.com/introduction/flow/):
    * 'package': launch an install/test/check on each push and pull request on 'main' branch.
    * 'release": on each tag push, launch:
      - a github release 
      - a pypi publish . You have to add a Trusted Publisher to an existing PyPI project(https://docs.pypi.org/trusted-publishers/adding-a-publisher/).
      - a site documentation publication
  * [dependabot](https://github.com/dependabot) to manage dependencies updates.
* Documentation:
  * Docstring styling with `pydocstyle`
  * Building documentation with `mkdocs`
  * Auto generation of API reference
  * Expose with documentation site under 'gh-pages' branch per default.


Until 2025/01/15, I use [poetry](https://python-poetry.org/) to rules them all. This work is still avalaible on `poetry`branch.


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
- Since python 3.12 and [PEP 696](https://peps.python.org/pep-0696/): I quit [mypy](https://mypy-lang.org/) for [pyright](https://github.com/microsoft/pyright), type checking should never be a pain...

In 2025, with the new release of poetry 2.0.0, I wanna make an update:

- use ruff as sucessor of isort and black (less dependency and tools)
- refactor poe the poet plugin installation with `tool.poetry.requires-plugins`
- simplify workflow and makefile
- update pyproject.toml declaration as our Python standard evolve :)

Few weeks later, my mates show me [uv](https://docs.astral.sh/uv/). An extremely fast Python package and project manager, written in Rust.
What I found very usefull:
- it's fast to resolve and install dependencies
- follow closely the pyproject.toml standardization
- more simple to manage than poetry
- you can handle complex dependencies nightmare https://docs.astral.sh/uv/concepts/resolution/, & see your dependencies tree...
- you can develop localy with unreleased libraries
- to build our library : we can use setuptools
This tool still missing something like poetthepoet, but i hope that it could be integrated soon.
So let's have a try !



## Usage

Install `cookiecutter` and generate a project:

```
$ pip install cookiecutter
$ cookiecutter gh:geronimo-iia/python-module-template -f
```

or using local clone and [uv](https://docs.astral.sh/uv/):

```
git clone git@github.com:geronimo-iia/python-module-template.git
cd python-module-template
make generate

```

Cookiecutter will ask you for some basic info (your name, project name, python package name, etc.) and generate a base Python project for you.

Poe target list:

| Name             | Comment                                  |
| ---------------- | ---------------------------------------- |
| poe types        | Run the type checker                     |
| poe lint         | Run linting tools on the code base       |
| poe style        | Validate black code style                |
| poe test         | Run unit tests                           |
| poe check        | Run all checks on the code base          |
| poe build        | Builds module                            |
| poe publish      | Publishes the package                    |
| poe docs         | Builds  site documentation.              |
| poe docs-publish | Build and publish site documentation.    |
| poe clean        | Delete all generated and temporary files |
| poe requirements | Generate requirements.txt                |
|                  |                                          |

You could retrieve those commands with `poe`. It will output something like this :

```
Usage:
  poe [global options] task [task arguments]

Global options:
  -h, --help            Show this help page and exit
  --version             Print the version and exit
  -v, --verbose         Increase command output (repeatable)
  -q, --quiet           Decrease command output (repeatable)
  -d, --dry-run         Print the task contents but don't actually run it
  -C PATH, --directory PATH
                        Specify where to find the pyproject.toml
  -e EXECUTOR, --executor EXECUTOR
                        Override the default task executor
  --ansi                Force enable ANSI output
  --no-ansi             Force disable ANSI output

Configured tasks:
  types                 Run the type checker
  lint                  Run linting tools on the code base
  style                 Validate black code style
  test                  Run unit tests
  check                 Run all checks on the code base
  build                 Build module
  publish               Publish module
  docs                  Build site documentation
  docs-publish          Publish site documentation
  clean                 Remove all generated and temporary files
  requirements          Generate requirements.txt

```


Make Target list:

| Name         | Comment                      |
| ------------ | ---------------------------- |
| make install | Install project dependencies |
| make lock    | Lock project dependencies    |
|              |                              |


