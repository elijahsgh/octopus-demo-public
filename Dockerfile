FROM python:3.12-alpine3.18
RUN pip install poetry

ENV POETRY_NO_INTERACTION=1

EXPOSE 8000

WORKDIR /app

COPY myapp/pyproject.toml /app
COPY myapp/poetry.toml /app
COPY myapp/*.py /app
COPY myapp/templates /app/templates
COPY myapp/scripts /app/scripts
COPY myapp/assets /app/assets

RUN poetry install

ENTRYPOINT ["/usr/local/bin/poetry", "run", "fastapi", "run"]
