SHELL := /bin/bash
VIRTUAL_ENV := venv
PYTHON := ${VIRTUAL_ENV}/bin/python3
IMAGE_NAME := accessories-app

start-dev:
	${PYTHON} -m pip install -r requirements.txt

create-venv:
	python3 -m venv venv
	@echo "To activate venv you should type source ${VIRTUAL_ENV}/bin/activate"

build:
	docker build -t ${IMAGE_NAME}:latest .

run:
	docker run -d --name mycon -p 80:80 ${IMAGE_NAME}

clean:
	rm -r ${VIRTUAL_ENV}