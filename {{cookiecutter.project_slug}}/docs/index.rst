Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================
Copyright (c) {% now 'local', '%Y' %} Be The Match operated by National Marrow Donor Program. All Rights Reserved.

Contents:

.. toctree::
   :maxdepth: 2

   readme
   installation
   usage
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors{% endif -%}
   history

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
