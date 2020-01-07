======================
Cookiecutter PyPackage
======================

.. image:: https://pyup.io/repos/github/audreyr/cookiecutter-pypackage/shield.svg
     :target: https://pyup.io/repos/github/audreyr/cookiecutter-pypackage/
     :alt: Updates

.. image:: https://travis-ci.org/audreyr/cookiecutter-pypackage.svg?branch=master
    :target: https://travis-ci.org/audreyr/cookiecutter-pypackage     

Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/audreyr/cookiecutter-pypackage/
* Documentation: https://cookiecutter-pypackage.readthedocs.io/
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``py.test``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.7, 3.5, 3.6
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* bump2version_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    $ cookiecutter https://github.com/nmdp-bioinformatics/cookiecutter-pypackage

    full_name [Pradeep Bashyal]:
    email [pbashyal@nmdp.org]:
    github_username [pbashyal-nmdp]:
    project_name [Python Project Example]:
    project_slug [python_project_example]:
    project_short_description [Python Boilerplate contains all the boilerplate you need to create a Python package.]:
    pypi_username [pbashyal-nmdp]:
    version [0.0.1]:
    use_pytest [n]:
    use_pypi_deployment_with_travis [y]:
    Select command_line_interface:
    1 - Click
    2 - No command-line interface
    Choose from 1, 2 [1]: 2
    create_author_file [y]:
    Select open_source_license:
    1 - LGPL 3.0
    2 - Not open source
    Choose from 1, 2 [1]: 1


Then:

* Create a repo and put it there.  Run ``make git-init``
* Install the dev requirements into a virtualenv. ``make venv``
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Run your tests with ``make test``
* Build your project with ``make dist``

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/distributing/#register-your-project

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html

