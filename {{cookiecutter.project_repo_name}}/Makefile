.PHONY: env run test lint requires docs
.DEFAULT: env

env:
	@python -m venv .venv
	@poetry install

run:
	@poetry run python {{ cookiecutter.project_repo_name }}/{{ cookiecutter.project_repo_name }}.py

test:
	@poetry run coverage run --branch -m unittest discover --pattern=tests/*.py && poetry run coverage html

requires:
	@poetry export -f requirements.txt --output requirements.txt

requires-dev:
	@poetry export -f requirements.txt --output requirements-dev.txt --dev

lint:
	@poetry run isort --virtual-env .venv {{ cookiecutter.project_repo_name }}/*.py && poetry run black .

docs:
	@poetry run sphinx-apidoc -f -o docs/source/ {{cookiecutter.project_repo_name}} ./tests/*.py
	@cd docs && make html
