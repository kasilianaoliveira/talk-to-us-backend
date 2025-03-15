FROM python:3.13-slim

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'


COPY ./poetry.lock /
COPY ./pyproject.toml /

