FROM python:3.9.4
# Allows the service to print to STDOUT without buffering
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install
