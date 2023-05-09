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


## Features

* Core:
  * [poetry](https://python-poetry.org/) to rules them all
  * [pep-0518](https://www.python.org/dev/peps/pep-0518/) alias `pyproject.toml` for managing dependencies, package metadata, ...
* Project tooling:
  * Setup formatting with [isort](https://github.com/PyCQA/isort) and [black](https://github.com/psf/black)
  * Analysing with [ruff](https://github.com/charliermarsh/ruff)
  * Type checking with `mypy`
  * Running tests with `pytest`
* Preconfigured setup for:
  * `Makefile` for automating common development tasks
  * [Github workflow](https://guides.github.com/introduction/flow/)
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


Make Target list:

| Name                 | Comment                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------- |
|                      |                                                                                          |
| debug-info           | Show poetry debug info                                                                   |
| install              | Install project dependencies                                                             |
| check                | Run linters and static analysis                                                          |
| test                 | Run unit tests                                                                           |
| build                | Builds the source and wheels archives                                                    |
| publish              | Publishes the package, previously built with the build command, to the remote repository |
| docs                 | Build and publish sit documentation.                                                     |
| clean                | Delete all generated and temporary files                                                 |
|                      |                                                                                          |
