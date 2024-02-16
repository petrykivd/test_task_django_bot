@echo off

python -m venv env
call env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

start python manage.py runserver

start python manage.py bot