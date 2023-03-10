.PHONY: help setup_venv setup_dependencies test lint

SRC_CODE:="src"
COVERAGE_THRESH:="90"

help:
	@echo "\Commands:"
	@echo "\tsetup_venv:    Set up the virtual environment."
	@echo "\ttest:          Run tests."
	@echo "\tlint:          Run linting test."
	@echo "\tchecks:          Run tests and lint"

setup_venv:
	python3 -m venv .venv && . .venv/bin/activate \
	&& python3 -m pip install --upgrade pip \
	&& python3 -m pip install -e .

train:
	. .venv/bin/activate && python ${SRC_CODE}/main.py

clean_pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean_test: # Remove prev test logs/artifacts
	rm -f .coverage
	rm -f .coverage.*
	find . -name '.pytest_cache' -exec rm -fr {} +

clean: clean_pyc clean_test
	find . -name '.my_cache' -exec rm -fr {} +
	rm -rf logs/

test: clean
	. .venv/bin/activate \
	&& pytest -svv --cov=${SRC_CODE} \
	tests --cov-report=term-missing \
	--cov-fail-under ${COVERAGE_THRESH}

lint:
	. .venv/bin/activate \
	&& black ${SRC_CODE} && isort ${SRC_CODE} \
	&& pylint ${SRC_CODE} -j 4 --reports=y

checks: test lint
