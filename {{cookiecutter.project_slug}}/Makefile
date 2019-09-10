.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 {{ cookiecutter.project_slug }} tests

test: ## run tests quickly with the default Python
{%- if cookiecutter.use_pytest == 'y' %}
	py.test
{%- else %}
	python setup.py test
{%- endif %}

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
{%- if cookiecutter.use_pytest == 'y' %}
	coverage run --source {{ cookiecutter.project_slug }} -m pytest
{%- else %}
	coverage run --source {{ cookiecutter.project_slug }} setup.py test
{%- endif %}
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/{{ cookiecutter.project_slug }}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{ cookiecutter.project_slug }}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

venv: ## creates a Python3 virtualenv environment in venv
	virtualenv -p python3 venv
	@echo "====================================================================="
	@echo "To activate the new virtualenv, execute the following from your shell"
	@echo "source $(PWD)/venv/bin/activate"

activate: ## activate a virtual environment. Run `make venv` before activating.
	@echo "====================================================================="
	@echo "To activate the new virtualenv, execute the following from your shell"
	@echo "source $(PWD)/venv/bin/activate"

git-init: ## initializes a git repository. Commits and pushes to github.
	@echo "====================================================================="
	@echo "Make sure you've created a github repo '{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}'"
	@read -p "Continue? [Y/N] " choice; \
	case "$$choice" in \
		y | Y ) \
			echo "====================================================================="; \
			git init . ; \
			git add . ; \
			git commit -m "Initial Import" ; \
			git remote add origin https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}} ; \
			git push -u origin master; \
			echo "====================================================================="; \
			echo "Git Initialized!" \
			;; \
	  * ) echo "Git NOT initialized!" ;; \
	esac; 

