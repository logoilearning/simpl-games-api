#!/bin/bash
./wait-for-it.sh -h db -p 5432 -t 20 -- python manage.py migrate
python manage.py create_simpl_user
python manage.py runserver 0.0.0.0:8100
