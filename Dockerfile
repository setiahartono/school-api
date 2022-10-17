FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN pip install -U pipenv

ADD Pipfile ./
ADD Pipfile.lock ./
RUN pipenv install --deploy --system
ADD . ./