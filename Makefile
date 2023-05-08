lint:
	pipenv run black src/ tests/
	pipenv run isort src/ tests/

test:
	pipenv run pytest -v

clean:
	rm *.json