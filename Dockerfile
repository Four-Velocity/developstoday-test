FROM python:3.8

RUN mkdir /app
WORKDIR /app

ADD news /app/
ADD Pipfile Pipfile.lock /app/

ENV PYTHONDONTWRITBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

ENV PORT=8888

RUN pip3 install --upgrade pip
RUN pip3 install pipenv

RUN pipenv install --system --dev

EXPOSE 8888
CMD gunicorn news.wsgi:application --bind 0000:$PORT