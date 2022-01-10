# Base Image
FROM python:3.7 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.7

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app/. app/.
COPY ./credentials/. credentials/.

ENV GOOGLE_APPLICATION_CREDENTIALS="../credentials/blog-336513-e0dbc5928c6f.json"

WORKDIR /code/app

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"] 