.PHONY: env run tests docs
.DEFAULT: env

env:
	@pipenv install --dev

run:
	@pipenv run python {{ cookiecutter.project_repo_name }}/{{ cookiecutter.project_repo_name }}.py

tests:
	@pipenv run python -m unittest tests

docs:
	@cd docs && make html

docs-init:
	@sphinx-apidoc
