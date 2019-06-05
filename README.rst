======================
Cookiecutter PyPackage
======================

Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/audreyr/cookiecutter-pypackage/
* Documentation: https://cookiecutter-pypackage.readthedocs.io/
* Free software: BSD license

.. _Cookiecutter: https://github.com/audreyr/cookiecutter


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

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Run the script `travis_pypi_setup.py` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to master.
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Activate your project on `pyup.io`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html
