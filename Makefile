SHELL := /bin/bash
VIRTUAL_ENV := venv
PYTHON := ${VIRTUAL_ENV}/bin/python3
IMAGE_NAME := accessories-web
IMAGE_PARSE_NAME := parse

start-dev:
	${PYTHON} -m pip install -r requirements.txt

create-venv:
	python3 -m venv venv
	@echo "To activate venv you should type source ${VIRTUAL_ENV}/bin/activate"

build:
	docker build -t ${IMAGE_NAME}:latest . && \
	docker build -t ${IMAGE_PARSE_NAME}:latest -f DockerfileParse .


run:
	docker compose up --build

clean:
	rm -r ${VIRTUAL_ENV}