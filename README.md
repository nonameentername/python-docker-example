python-docker-example
=====================

Example on using docker and fig for python development

Install [docker](https://docs.docker.com/installation/)

Install fig

    pip install fig

Run riak backend for development:

    fig -f dev.yml up

Run demo application:

    fig up
