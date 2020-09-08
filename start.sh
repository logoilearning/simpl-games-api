#!/bin/bash
./wait-for-it.sh -h $DB_HOST -p $DB_PORT -t 20 -- python manage.py migrate
python manage.py collectstatic --noinput
gunicorn -c /code/gunicorn.conf 'config.wsgi'
