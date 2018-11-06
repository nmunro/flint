.PHONY: env run tests docs
.DEFAULT: env

env:
	@poetry install

run:
	@poetry run python {{ cookiecutter.project_repo_name }}/{{ cookiecutter.project_repo_name }}.py

test:
	@poetry run coverage run --branch -m unittest discover; poetry run coverage html

lint:
	@poetry run isort --virtual-env .venv {{ cookiecutter.project_repo_name }}/*.py && poetry run coala all

docs:
	@poetry run sphinx-apidoc -f -o docs/source/ {{cookiecutter.project_repo_name}} ./tests/*.py
	@cd docs && make html
