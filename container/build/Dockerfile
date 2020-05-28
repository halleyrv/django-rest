FROM python:3.7.4

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    libcurl4-openssl-dev \
    libssl-dev \
    vim


RUN mkdir /code
COPY . /code/
WORKDIR /code/application


RUN pip install --upgrade pip && pip install pipenv && pipenv install --verbose
EXPOSE 5000
