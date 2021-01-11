# {{cookiecutter.project_name}}


[![Travis Build Status](https://img.shields.io/travis/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}/master.svg?label=unix)](https://travis-ci.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}})
[![Codecov](https://codecov.io/gh/geronimo-iia/async-btree/branch/master/graph/badge.svg?token=SXD9Z508CA)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}})
[![PyPI Version](https://img.shields.io/pypi/v/{{cookiecutter.github_repo}}.svg)](https://pypi.org/project/{{cookiecutter.github_repo}})
[![PyPI License](https://img.shields.io/pypi/l/{{cookiecutter.github_repo}}.svg)](https://pypi.org/project/{{cookiecutter.github_repo}})

Versions following [Semantic Versioning](https://semver.org/)

## Overview

{{cookiecutter.project_short_description}}

## Installation

Install this library directly into an activated virtual environment:

```text
$ pip install {{cookiecutter.github_repo}}
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add {{cookiecutter.github_repo}}
```

## Usage

After installation, the package can imported:

```text
$ python
>>> import {{cookiecutter.package_name}}
>>> {{cookiecutter.package_name}}.__version__
```

See [documentation](https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.github_repo}}).
