# Set the base image to Ubuntu
FROM python:2.7

# File Author / Maintainer
MAINTAINER Ujjwal Wahi

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

ADD . /code/

# create unprivileged user
RUN adduser --disabled-password --gecos '' ujjwal