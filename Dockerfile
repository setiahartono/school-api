FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN pip install pipenv

ADD requirements.txt ./

RUN pip install -r requirements.txt
ADD . ./