#!/bin/bash
./wait-for-it.sh -h $DB_HOST -p $DB_PORT -t 20 -- python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8100
# gunicorn -c /code/gunicorn.conf 'config.wsgi'
