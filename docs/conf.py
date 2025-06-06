# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

import sphinx.application
from sphinx.locale import get_translation

import iati_sphinx_theme

MESSAGE_CATALOG_NAME = "iati-web-terms"
_ = get_translation(MESSAGE_CATALOG_NAME)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "IATI Web Terms"
author = "IATI Secretariat"
language = "en"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "iati_sphinx_theme"
html_theme_options = {
    "github_repository": "https://github.com/IATI/web-terms",
    "languages": ["en", "fr"],
    "project_title": _("IATI Web Terms"),
    "header_title_text": _("IATI Web Terms"),
    "header_eyebrow_text": "IATI",
}

todo_include_todos = True

# -- Options for Texinfo output -------------------------------------------

locale_dirs = [
    "locale",
    os.path.join(os.path.dirname(iati_sphinx_theme.__file__), "locale"),
]


def setup(app: sphinx.application.Sphinx) -> None:
    locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "locale")
    app.add_message_catalog(MESSAGE_CATALOG_NAME, locale_path)