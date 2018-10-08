FROM debian:latest

MAINTAINER Gosha Chernousov

RUN apt-get update && apt-get install -y apache2 \
libapache2-mod-wsgi-py3 \
python3-pip \
python3-dev \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

COPY ./app/requirements.txt /var/www/integration_1c/app/requirements.txt
RUN pip3 install -r /var/www/integration_1c/app/requirements.txt \
&& pip3 install --upgrade google-auth-oauthlib

COPY ./integration_1c.conf /etc/apache2/sites-available/integration_1c.conf
RUN a2ensite integration_1c \
&& a2enmod headers

COPY ./integration_1c.wsgi /var/www/integration_1c/integration_1c.wsgi

COPY ./run.py /var/www/integration_1c/run.py
COPY ./app /var/www/integration_1c/app/

RUN a2dissite 000-default.conf \
&& a2ensite integration_1c.conf


EXPOSE 80

WORKDIR /var/www/integration_1c

CMD  /usr/sbin/apache2ctl -D FOREGROUND
