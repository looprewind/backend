#!/bin/sh

init:
	sudo docker-compose run web python manage.py migrate

run:
	sudo docker-compose up -d --build

stop:
	sudo docker-compose down

test:
	sudo docker-compose run web python manage.py test apps/youtube/tests

# debug purpose
build:
	sudo docker-compose build

run-cmd:
	sudo docker-compose up
