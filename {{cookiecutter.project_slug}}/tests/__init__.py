# -*- coding: utf-8 -*-
{% if cookiecutter.open_source_license == 'LGPL 3.0' %}
{% include 'HEADER.txt' %}
{% else %}
# Copyright (c) {% now 'local', '%Y' %} Be The Match operated by National Marrow Donor Program. All Rights Reserved.
{% endif %}
