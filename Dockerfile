FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD . /code/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
ENV DJ_SETTINGS core.settings_docker