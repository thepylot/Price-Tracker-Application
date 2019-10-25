# Price-Tracker-Application
Discount Tracker app with Python/Django

## Getting Started

This tutorial works on **Python 3+** and Django 2+.

Install dependencies:

```
python3 -m pip3 install -r requirements.txt
```
start Celery worker:

```
celery -A randompostgenerator worker -l info
```
and run following commands:

```
python3 manage.py makemigrations tracker
python3 manage.py migrate
python3 manage.py runserver
```
