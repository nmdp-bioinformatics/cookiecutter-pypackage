Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================
Copyright (c) {% now 'local', '%Y' %} Be The Match operated by National Marrow Donor Program. All Rights Reserved.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   installation

   {{cookiecutter.project_slug}}

   usage
   modules
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {% endif -%}history

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
