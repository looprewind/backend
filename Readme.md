# Relief Backend

## About me

As you may have notice, I'm not an expert on Frontend technologies hahahahahaha. So I try to make an interesting Backend,
 is one of my strengths, although I have a lot to learn!

## About the project

I have no idea what software you have on your computer (and which versions!) so I decided to dockerize the project.
There's a Makefile that easily run all the commands you need, don't worry :wink:
The main concept it's that there are two services (containers) running:
* Django backend: I tryed to focus more on a REST API concept that on a traditional Django App, so I decided to use
 Django Rest Framework (DRF).
* PostgreSQL: although an SQLite db it's quite enought for a project like this, I'm not a big fan of using a shared/versioned
.sqlite file, so there's a PSQL service that will run on your computer and will store every change you make!

## Requirements

You need to **install docker** and **docker-compose** installed on your pc to run this project! If your using a Debian based OS,
you can easy intall it with:

```shell script
sudo apt update
sudo apt install docker.io docker-compose
```

## Run the project

First you have to init the project and then run it with:

```shell script
make init
make run 
```

To stop all the containers use:

```shell script
make stop 
```

## Tests

To run the tests (with the services running)  use:

```shell script
make test 
```

Also you can GET all the saved URL's in your db with:

```shell script
curl --location --request GET 'http://localhost:8000/'
```

or POST one with:

```shell script
curl --location --request POST 'http://localhost:8000/' \
--form 'url=https://www.youtube.com/watch?v=nSKp2StlS6s'
```

# TODO's

* Pagination: this is a small project, but its always a good practice to include it
* Secure way to connect to the database: it's not a good practice to use the default user

---
Thanks a lot for your time, feedback it's always welcomed! :thumbsup: