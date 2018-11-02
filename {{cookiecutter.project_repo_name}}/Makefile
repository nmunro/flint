.PHONY: env run tests docs
.DEFAULT: env

env:
	@pipenv install --dev

run:
	@pipenv run python {{ cookiecutter.project_repo_name }}/{{ cookiecutter.project_repo_name }}.py

test:
	@pipenv run coverage run --branch -m unittest discover; pipenv run coverage html

lint:
	@pipenv run isort --virtual-env .venv {{ cookiecutter.project_repo_name }}/*.py && pipenv run coala all

docs:
	@pipenv run sphinx-apidoc -f -o docs/source/ {{cookiecutter.project_repo_name}} ./tests/*.py
	@cd docs && make html
