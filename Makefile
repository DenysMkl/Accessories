SHELL := /bin/bash
VIRTUAL_ENV := venv
PYTHON := ${VIRTUAL_ENV}/bin/python3
IMAGE_NAME := accessories-app

start-dev: create-venv
	${PYTHON} -m pip install -r requirements.txt

create-venv:
	python3 -m venv venv

build:
	docker build -t ${IMAGE_NAME}:latest .

clean:
	rm -r ${VIRTUAL_ENV}