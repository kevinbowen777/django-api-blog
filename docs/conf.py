"""Sphinx configuration."""

project = "django-api-blog"
author = "Kevin Bowen"
copyright = f"2024, {author}"
#
html_theme = "furo"
html_logo = "django_24.png"
html_title = "django-api-blog"
extensions = [
    "sphinx.ext.duration",
]
