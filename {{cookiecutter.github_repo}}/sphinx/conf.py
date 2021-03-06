# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

import toml


sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), "..",)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), "..", "{{cookiecutter.package_name}}")))


# -- Project information -----------------------------------------------------

def get_version():
    """Return current project version from pyproject.toml."""

    toml_path = os.path.join(os.path.dirname(__file__), "..", "pyproject.toml")
    with open(toml_path, "r") as fopen:
        pyproject = toml.load(fopen)
    return pyproject["tool"]["poetry"]["version"]


project = '{{cookiecutter.package_name}}'
copyright = '{{cookiecutter.year}}, {{cookiecutter.full_name}}'
author = '{{cookiecutter.full_name}} <{{cookiecutter.email}}>'

# The full version, including alpha/beta/rc tags
release = get_version()


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.ifconfig",
    "sphinx.ext.autosummary",
    "m2r",
    "autodocsumm",
]

autoclass_content = "both"  # include both class docstring and __init__
autosummary_generate = True

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# autodocsumm settings
autodoc_default_options = {'autosummary': True}

# Autodoc Settings
autodoc_default_options = {"member-order": "bysource", "undoc-members": True, "members": True, "show-inheritance": True}

source_suffix = ['.rst', '.md']

# Autodoc Settings
autodoc_default_options = {"member-order": "bysource", "undoc-members": True}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Set master doc
master_doc = "index"
