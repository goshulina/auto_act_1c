FROM debian:latest

MAINTAINER Gosha Chernousov

RUN apt-get update && apt-get install -y python3-pip \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

COPY . /var/www/integration_1c/

RUN pip3 install -r /var/www/integration_1c/requirements.txt \
&& pip3 install --upgrade google-auth-oauthlib

EXPOSE 80

WORKDIR /var/www/integration_1c

RUN python3 main.py