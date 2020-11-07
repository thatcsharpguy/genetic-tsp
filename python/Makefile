PIPENV := pipenv run

BLACK_TARGETS := $(shell find . -name "*.py" -not -path "*/.venv/*" -not -path "*/.tox/*")


format:
	$(PIPENV) isort . --apply
	$(PIPENV) black $(BLACK_TARGETS)
.PHONY: format

lint:
	$(PIPENV) black --check $(BLACK_TARGETS)
.PHONY: lint