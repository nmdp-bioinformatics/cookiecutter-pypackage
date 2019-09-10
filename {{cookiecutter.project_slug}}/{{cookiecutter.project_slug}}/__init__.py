# -*- coding: utf-8 -*-
{% if cookiecutter.open_source_license == 'LGPL 3.0' %}
{% include 'HEADER.txt' %}
{% else %}
# Copyright (c) {% now 'local', '%Y' %} Be The Match operated by National Marrow Donor Program. All Rights Reserved.
{% endif %}

"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'
