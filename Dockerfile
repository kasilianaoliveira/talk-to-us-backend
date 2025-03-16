FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH=/

COPY ./poetry.lock /
COPY ./pyproject.toml /
COPY ./README.md /


RUN apt-get update -y && \
    apt-get install -y pipx && \
    pipx ensurepath && \
    pipx install poetry && \
    rm -rf /root/.cache/pypoetry && \
    poetry install --no-root && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./src /src
WORKDIR /src
