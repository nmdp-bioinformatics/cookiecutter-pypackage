# -*- coding: utf-8 -*-
{% if cookiecutter.open_source_license == 'LGPL 3.0' %}
{% include 'HEADER.txt' %}
{% else %}
# Copyright (c) {% now 'local', '%Y' %} Be The Match operated by National Marrow Donor Program. All Rights Reserved.
{% endif %}

import click


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}"""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
