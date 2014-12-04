# riak
#
# VERSION               0.1

FROM ubuntu:14.04
MAINTAINER Werner R. Mendizabal "werner.mendizabal@gmail.com"

RUN apt-get update

RUN apt-get install -y python-pip python-dev git-core libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev

RUN pip install -U pip

RUN apt-get install -y libffi-dev

ADD . /code

WORKDIR /code

ENV PBR_VERSION 0.10.0

RUN python setup.py install

EXPOSE 8080

CMD python -m demo.app
