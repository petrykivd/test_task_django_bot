#!/bin/bash

python -m venv env
source env/bin/activate

pip install -r requirements.txt

python3 manage.py migrate

python3 manage.py runserver localhost:8000 &

python3 manage.py bot &