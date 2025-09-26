# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import subprocess
from datetime import datetime

import sphinx.application
from sphinx.locale import get_translation

import iati_sphinx_theme

MESSAGE_CATALOG_NAME = "iati-web-terms"
_ = get_translation(MESSAGE_CATALOG_NAME)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

def get_privacy_policy_last_commit_date():
    """Get the date of the last commit that affected privacy-policy.rst, websites.rst, or cookie-policy.rst"""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cd", "--date=format:%d %B %Y",
             "--", "docs/privacy-policy.rst", "docs/websites.rst", "docs/cookie-policy.rst"],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.dirname(__file__))
        )
        return result.stdout.strip()
    except Exception:
        return datetime.now().strftime("%d %B %Y")

project = "IATI Web Terms"
author = "IATI Secretariat"
language = "en"

# Global variables available in RST files
rst_prolog = f"""
.. |privacy_policy_effective_date| replace:: {get_privacy_policy_last_commit_date()}
"""

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