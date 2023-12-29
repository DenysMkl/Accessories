FROM python:3.10

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY ./requirements.txt /code/
COPY ./Makefile /code/

RUN make start-dev

COPY . /code/

CMD ["uvicorn", "accessories.cases_api:app", "--reload"]