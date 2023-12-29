SHELL := /bin/bash
VIRTUAL_ENV := venv
PYTHON := ${VIRTUAL_ENV}/bin/python3

start-dev: create-venv
	${PYTHON} -m pip install -r requirements.txt

create-venv:
	python3 -m venv venv

clean:
	rm -r ${VIRTUAL_ENV}