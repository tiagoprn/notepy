# notepy 

Personal notes accessible from Django Admin and a Rest API, with versioning and markdown support. 

Created based on this recipe: https://github.com/tiagoprn/experiments/tree/master/django/drf_book

## How to run the project 

```
$ pip install -r requirements.txt (please do this on a virtualenv)
$ cd notes_api
$ python manage.py migrate
$ python manage.py createsuperuser (this user will be used to login to the API, which will support permissions on a few iterations on the future).
$ python manage.py collectstatic (this will copy the django-admin/drf console static files to /static)
$ cd static && python -m http.server 8088 & (this will run python's http server to serve the static files)
$ python manage.py runserver
```

