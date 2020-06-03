#!/bin/bash

python ./manage.py migrate
gunicorn news.wsgi:application --bind 0000:8888 --daemon
#python ./manage.py runserver 0.0.0.0:8888
