# -----IMPORTANT-----
# -----CODE EMPRUNTÉ-----
# le fichier a été créer en suivant un tutoriel dans le lien suivant :
# https://sourcery.ai/blog/python-docker/
# J'ai changé quelque petite ligne, mais la grande majorité du code est
# le même que le tutoriel.

## To implement
FROM python:3.9-alpine AS base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Install application into container
COPY . .

# Run the application
ENTRYPOINT ["python", "src/main.py"]
