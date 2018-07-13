FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /blog_app
ADD . /blog_app

RUN pip install -r requirements.txt