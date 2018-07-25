FROM ubuntu:18.04

RUN apt-get update &&\
    apt-get -y install \
        build-essential \
        libssl-dev \
        libffi-dev \
        python-dev \
        python-pip

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt
