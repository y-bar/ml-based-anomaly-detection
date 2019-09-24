AUTOFLAKE_OPTS := --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports --recursive --in-place
SOURCES := sranodec tests

.PHONY: prepare
prepare:
	pip install pipenv
	pipenv install --dev

.PHONY: lint
lint:
	pipenv run autoflake $(AUTOFLAKE_OPTS) --check $(SOURCES)
	pipenv run black --check $(SOURCES)
	pipenv run isort --recursive --check-only $(SOURCES)

.PHONY: format
format:
	pipenv run autoflake $(AUTOFLAKE_OPTS) $(SOURCES)
	pipenv run black $(SOURCES)
	pipenv run isort --recursive $(SOURCES)

.PHONY: test
test:
	pipenv run pytest tests