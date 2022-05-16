This PoC was needed to check if Django-CQRS or Django-RQL can work with Django-Mongoengine on top of Atlas MongoDB.

Verdict:
* Django-CQRS can work with slight modifications
* Django-RQL doesn't work at all and a separate library must be developed

Requirements
==========

Python 3.10


Trying out
==========

1. Set env variables for Mongo configuration:
```python
MONGODB_DATABASES = {
    'default': {
        'name': os.environ.get('MONGO_NAME'),
        'host': os.environ.get('MONGO_HOST'),
        'password': os.environ.get('MONGO_PASSWORD'),
        'username': os.environ.get('MONGO_USER'),
        'tz_aware': USE_TZ,
    },
}
```
2. Play around in Django shell:
```commandline
pip install -r requirements.txt
python manage.py shell
```
