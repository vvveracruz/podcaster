lint:
	pipenv run black src/
	pipenv run isort src/

test:
	pipenv run pytest