# DevelopsToday Test Task
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/18c701636f61fee3f8a8)
[![Heroku](https://www.herokucdn.com/deploy/button.svg)](https://developstoday-test.herokuapp.com)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge&logo=appveyor)](https://github.com/psf/black)
[![Linter: Flake8](https://img.shields.io/badge/Linter-Flake8-9cf?style=for-the-badge&logo=appveyor)](https://pypi.org/project/flake8/)
[![Type Checker: PyRight](https://img.shields.io/badge/type%20checker-PyRight-9cf?style=for-the-badge&logo=appveyor)](https://github.com/microsoft/pyright)

So. Here is the test task)
Some points to clarify

## Launching
To run this app you have to:
* ~~Add *.env* file to root *or you can just rename .env.example to .env and the app has to work*~~
* Change *.env* if you want, but everything will work correctly if you pass this step
* Run
```
$ docker-compose build
$ docker-compose up web
```
* The server will be running on [http://localhost](http://localhost)
* Migrations apply automatically, however if you want to use admin page you must create superuser 
* Upvotes reset now runs automatically every 24 hours using [cron](news/bash/cron.sh) with [this preset](news/bash/cron-setup). As for the running style it was taken from [here](https://docs.docker.com/config/containers/multi-service_container/)
* To apply upvotes reset manually run `$ docker-compose run web python manage.py runcrons` while the web docker container is running

## Hosting
The copy of this app is running on [Heroku](https://developstoday-test.herokuapp.com)    
I leave `DEBUG = True` so you will see what's wrong if smt. occurs  
Also there is a superuser with login: `admin` and password: `SupaStrong`, so you can use admin page if you need it

There are 2 heroku addons running alongside docker container:
* Heroku postgres
* Heroku scheduler (heroku cron analog)

Upvotes reset runs every 10 minutes instead of 24 hours, so you can test it

## Code Style
During the whole codding session I was using [Flake8](https://pypi.org/project/flake8/) and [PyRight](https://github.com/microsoft/pyright).  
After that the whole project was reformated by Black.

About errors:
* Several with Flake8, 'cause the strings are to long
* One with PyRight, in [cron.py](news/news/cron.py) with import, but it works nice :confused:

## Why django-cron, not celery?
The answer is simple, I find this package more lightweight.
Also in my opinion for purpose of resetting upvotes the api endpoint format *http://example.com/api/reset_upvotes/?key=SUPA_SECRAT_KEY/* and simple curl request in cron would be also good solution, but I think it's too late to change something.
