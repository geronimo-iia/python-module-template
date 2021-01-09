# {{cookiecutter.project_name}}


[![Travis Build Status](https://img.shields.io/travis/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}/master.svg?label=unix)](https://travis-ci.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}})
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fe669a02b4aa46b5b1faf619ba2bf382)](https://www.codacy.com/app/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}?utm_source=github.com&amp;utm_medium=referral&amp;utm_content={{cookiecutter.github_username}}/{{cookiecutter.github_repo}}&amp;utm_campaign=Badge_Grade)
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
