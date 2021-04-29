FROM python:3.9.2

WORKDIR /app
COPY . .
RUN pip install poetry
RUN poetry install
RUN pip install pendulum
RUN pip install pymongodb
WORKDIR /app/src
ENTRYPOINT python /app/src/main.py
