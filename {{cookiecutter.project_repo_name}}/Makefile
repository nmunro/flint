.PHONY: env run tests docs
.DEFAULT: env

env:
	@pipenv install --dev

run:
	@pipenv run python {{ cookiecutter.project_repo_name }}/{{ cookiecutter.project_repo_name }}.py

tests:
	@pipenv run python -m unittest tests

docs:
	@sphinx-apidoc -o docs/source/ ../{{ cookiecutter.project_repo_name }}/
	@cd docs && make html
