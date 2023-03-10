"""Sphinx configuration."""
project = "Cookiecutter Hypermodern Python Instance"
author = "Gareth Stockwell"
copyright = "2023, Gareth Stockwell"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
