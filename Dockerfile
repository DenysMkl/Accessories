FROM python:3.10

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY ./requirements.txt /app/
COPY ./Makefile /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["uvicorn", "Accessories.accessories.cases_api:app", "--host", "0.0.0.0", "--reload"]
