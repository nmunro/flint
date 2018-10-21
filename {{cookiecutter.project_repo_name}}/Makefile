.PHONY: env run tests docs
.DEFAULT: env

env:
	@pipenv install --dev

run:
	@pipenv run python {{ cookiecutter.project_repo_name }}/{{ cookiecutter.project_repo_name }}.py

test:
	@pipenv run coverage run --branch -m unittest discover; pipenv run coverage html

lint:
	@pipenv run isort

docs:
	@sphinx-apidoc -o docs/source/ ../{{ cookiecutter.project_repo_name }}/
	@cd docs && make html
