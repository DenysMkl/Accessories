FROM python:3.10

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . /code/

#RUN chmod +x ./entrypoint.sh
#RUN ./entrypoint.sh parse

CMD ["./entrypoint.sh"]
