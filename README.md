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
* Add .env file to root *or you can just rename .env.example to .env and the app has to work*
* run
```
$ docker-compose build
$ docker-compose run
```
* The server will be running on [http://localhost](http://localhost)
* Migrations apply automatically, however if you want to use admin page you must create superuser  
* Additional you can change some variables in .env file, but they are already set up for properly work  

## Hosting
The copy of this app is running on [Heroku](https://developstoday-test.herokuapp.com)    
I leave `DEBUG = True` so you will see what's wrong if smt. occurs  
Also there is a superuser with login: `admin` and password: `SupaStrong`, so you can use admin page if you need it


## Code Style
During the whole codding session I was using [Flake8](https://pypi.org/project/flake8/) and [PyRight](https://github.com/microsoft/pyright).  
After that the whole project was reformated by Black.

About errors:
* Several with Flase8, 'cause the strings are to long
* One with PyRight, in [cron.py](news/news/cron.py) with import, but it works nice :confused:
