.. _`changelog`:

=========
Changelog
=========

``django-api-blog`` issues are filed on `GitHub <https://github.com/kevinbowen777/django-api-blog/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

django-api-blog 0.3.7 (2026-10-01)
==================================

Improved documentation
----------------------

-  (`#570 <https://github.com/kevinbowen777/django-api-blog/issues/570>`_): Link CHANGELOG to Sphinx documentation

-  (`#570 <https://github.com/kevinbowen777/django-api-blog/issues/570>`_): Add myst-parser dependency

-  (`#570 <https://github.com/kevinbowen777/django-api-blog/issues/570>`_): Add CONTRIBUTING document

-  (`#570 <https://github.com/kevinbowen777/django-api-blog/issues/570>`_): Restructure documentation


Contributor-facing changes
--------------------------

-  (`#570 <https://github.com/kevinbowen777/django-api-blog/issues/570>`_): Update django-countries to 9.1.0

-  (`#570 <https://github.com/kevinbowen777/django-api-blog/issues/570>`_): Update djlint to 1.46.2

-  (`#570 <https://github.com/kevinbowen777/django-api-blog/issues/570>`_): Update psycopg to 3.3.6

-  (`#570 <https://github.com/kevinbowen777/django-api-blog/issues/570>`_): Update werkzeug to 3.1.9

-  (`#620 <https://github.com/kevinbowen777/django-api-blog/issues/620>`_): Fix Coverage context warnings

-  (`#621 <https://github.com/kevinbowen777/django-api-blog/issues/621>`_): Fix FactoryBoy DeprecationWarning messages

-  (`#622 <https://github.com/kevinbowen777/django-api-blog/issues/622>`_): Fix Swagger/drf-yasg deprecation warnings


Security updated
----------------

-  (`#570 <https://github.com/kevinbowen777/django-api-blog/issues/570>`_): Update django-allauth to 65.19.6

django-api-blog 0.3.6 (2026-09-10)
==================================

Contributor-facing changes
--------------------------

-  (`#608 <https://github.com/kevinbowen777/django-api-blog/issues/608>`_): Initial zizmor remediation. Pin GitHub actions to hashes.

-  (`#611 <https://github.com/kevinbowen777/django-api-blog/issues/611>`_): Update testing to Python 3.14.7, 3.13.15, and 3.12.14

-  (`#611 <https://github.com/kevinbowen777/django-api-blog/issues/611>`_): Update nox to 2026.8.17

-  (`#611 <https://github.com/kevinbowen777/django-api-blog/issues/611>`_): Update django-debug-toolbar to 7.1.1

-  (`#616 <https://github.com/kevinbowen777/django-api-blog/issues/616>`_): Update django-debug-toolbar to 8.0.0

-  (`#616 <https://github.com/kevinbowen777/django-api-blog/issues/616>`_): Update django-allauth to 65.19.2

-  (`#616 <https://github.com/kevinbowen777/django-api-blog/issues/616>`_): Upgrade gunicorn to 26.2.0

-  (`#616 <https://github.com/kevinbowen777/django-api-blog/issues/616>`_): Update djlint to 1.46.1

-  (`#616 <https://github.com/kevinbowen777/django-api-blog/issues/616>`_): Update towncrier to 26.9.0

-  (`#616 <https://github.com/kevinbowen777/django-api-blog/issues/616>`_): Upgrade environs to 15.2.0

-  (`#616 <https://github.com/kevinbowen777/django-api-blog/issues/616>`_): Update psycopg to 3.3.5

-  (`#617 <https://github.com/kevinbowen777/django-api-blog/issues/617>`_): Replace master with main in static gh action

-  (`#618 <https://github.com/kevinbowen777/django-api-blog/issues/618>`_): Upgrade GitHub actions to latest versions


New features
------------

-  (`#616 <https://github.com/kevinbowen777/django-api-blog/issues/616>`_): Upgrade djangorestframework to 3.18.1

-  (`#616 <https://github.com/kevinbowen777/django-api-blog/issues/616>`_): Upgrade Django to 6.1.1

django-api-blog 0.3.5 (2026-08-20)
==================================

Improved documentation
----------------------

-  (`#585 <https://github.com/kevinbowen777/django-api-blog/issues/585>`_): Add towncrier 25.8.0.


New features
------------

-  (`#610 <https://github.com/kevinbowen777/django-api-blog/issues/610>`_): Upgrade to Django 6.0.8

django-api-blog 0.3.4 (2026-07-31)
==================================

Contributor-facing changes
--------------------------

-  (`#561 <https://github.com/kevinbowen777/django-api-blog/issues/561>`_): Add Python 3.14 support.

-  (`#604 <https://github.com/kevinbowen777/django-api-blog/issues/604>`_): Update with Python 3.14.6 & 3.13.14.

-  (`#606 <https://github.com/kevinbowen777/django-api-blog/issues/606>`_): Rename default branch to main.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#600 <https://github.com/kevinbowen777/django-api-blog/issues/600>`_): Drop support for Python 3.11.


New features
------------

-  (`#569 <https://github.com/kevinbowen777/django-api-blog/issues/569>`_): Upgrade Django to 6.0.7.

django-api-blog 0.3.3 (2025-05-06)
==================================

Contributor-facing changes
--------------------------

-  (`#504 <https://github.com/kevinbowen777/django-api-blog/issues/504>`_): Upgrade PostgreSQL to 15.11.

-  (`#515 <https://github.com/kevinbowen777/django-api-blog/issues/515>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#510 <https://github.com/kevinbowen777/django-api-blog/issues/510>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#509 <https://github.com/kevinbowen777/django-api-blog/issues/509>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#453 <https://github.com/kevinbowen777/django-api-blog/issues/453>`_): Upgrade Docker image to Python 3.13 & Poetry 2.1.1.

-  (`#514 <https://github.com/kevinbowen777/django-api-blog/issues/514>`_): Upgrade Django Rest Framework to 3.16.0.

-  (`#516 <https://github.com/kevinbowen777/django-api-blog/issues/516>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#519 <https://github.com/kevinbowen777/django-api-blog/issues/519>`_): Replace safety package with pip-audit.

django-api-blog 0.3.2 (2025-01-20)
==================================

Contributor-facing changes
--------------------------

-  (`#450 <https://github.com/kevinbowen777/django-api-blog/issues/450>`_): Add support for Python 3.13

-  (`#492 <https://github.com/kevinbowen777/django-api-blog/issues/492>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#483 <https://github.com/kevinbowen777/django-api-blog/issues/483>`_): Upgrade Django to 5.1.4

django-api-blog 0.3.0 (2023-12-22)
==================================

Contributor-facing changes
--------------------------

-  (`#190 <https://github.com/kevinbowen777/django-api-blog/issues/190>`_): Migrate to non-root Docker user & venv.

-  (`#349 <https://github.com/kevinbowen777/django-api-blog/issues/349>`_): Upgrade Poetry to 1.7.1.

-  (`#360 <https://github.com/kevinbowen777/django-api-blog/issues/360>`_): Update Python to 3.12.1.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#346 <https://github.com/kevinbowen777/django-api-blog/issues/346>`_): Drop support for Python 3.9.


Improved documentation
----------------------

- : Update Sphinx theme to Furo


New features
------------

-  (`#357 <https://github.com/kevinbowen777/django-api-blog/issues/357>`_): Upgrade to Django 5.0.

django-api-blog 0.2.0 (2023-05-15)
==================================

Contributor-facing changes
--------------------------

-  (`#202 <https://github.com/kevinbowen777/django-api-blog/issues/202>`_): Install ruff. Drop flake8-* packages.

django-api-blog 0.1.0 (2023-05-08)
==================================

Contributor-facing changes
--------------------------

- : Implement nox for testing

- : Mirror to GitLab.

-  (`#1 <https://github.com/kevinbowen777/django-api-blog/issues/1>`_): Migrate from pipenv to Poetry

-  (`#199 <https://github.com/kevinbowen777/django-api-blog/issues/199>`_): Add support for Python 3.12.

-  (`#205 <https://github.com/kevinbowen777/django-api-blog/issues/205>`_): Re-write for compatibility with Poetry 1.4.1.

-  (`#210 <https://github.com/kevinbowen777/django-api-blog/issues/210>`_): Upgrade PostgreSQL to 15.2

-  (`#227 <https://github.com/kevinbowen777/django-api-blog/issues/227>`_): Upgrade Django to 4.2.1

-  (`#5 <https://github.com/kevinbowen777/django-api-blog/issues/5>`_): Migrate from SQLite to PostgreSQL


Improved documentation
----------------------

- : Add Sphinx for documentation

django-api-blog 0.0.1 (2022-03-22)
==================================

Contributor-facing changes
--------------------------

- : Add support for Python 3.10


New features
------------

- : Support Django 4.0.4


Miscellaneous internal changes
------------------------------

- : Initial commit
