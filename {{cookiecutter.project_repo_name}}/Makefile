.PHONY: env run test lint requires deploy docs
.DEFAULT: env

env:
	@poetry install

run:
	@poetry run python {{ cookiecutter.project_repo_name }}/{{ cookiecutter.project_repo_name }}.py

test:
	@poetry run coverage run --branch -m unittest discover && poetry run coverage html

requires:
	@poetry show --no-dev | tr -s " " | sed 's/ /==/' | sed 's/ .*//' > requirements.txt

deploy:
	@git push -u heroku master

lint:
	@poetry run isort --virtual-env .venv {{ cookiecutter.project_repo_name }}/*.py && poetry run coala all

docs:
	@poetry run sphinx-apidoc -f -o docs/source/ {{cookiecutter.project_repo_name}} ./tests/*.py
	@cd docs && make html
