.EXPORT_ALL_VARIABLES:
SHELL=/bin/bash
ENV_FILE=../notepy.env
SET_VARIABLES=set -a && source ${ENV_FILE} && set +a &&

help:
	@echo 'create_migrations: create new migrations'
	@echo 'migrate: apply migrations'
	@echo 'versionate: create a initial version for all remaining models. It should be run each time you add a model to version control (django-revision)'
	@echo 'su: create superuser (user used to login to the admin and to the API)'
	@echo 'process_static: this will copy the django-admin/drf console static files to /static'
	@echo "static_server: this will run python's http server to serve the static files"
	@echo 'run: run the app'
	@echo 'urls: list all app available URLs.'
	@echo 'shell: get a bpython shell into the django app, auto-importing its models (django shell_plus)'
	@echo 'notebook: get a jupyter notebook shell into the django app, auto-importing its models (django shell_plus)'


create_migrations:
	bash -c "${SET_VARIABLES} python manage.py makemigrations notes"

migrate:
	bash -c "${SET_VARIABLES} python manage.py migrate"

versionate:
	bash -c "${SET_VARIABLES} python manage.py createinitialrevisions"

su: migrate
	bash -c "${SET_VARIABLES} python manage.py createsuperuser"

process_static:
	python manage.py collectstatic

static_server:
	cd static && python -m http.server 8088 &

run: migrate
	bash -c "${SET_VARIABLES} python manage.py runserver"

urls:
	python manage.py show_urls

shell:
	bash -c "${SET_VARIABLES} python manage.py shell_plus --ipython"

notebook:
	@echo 'IPython Notebooks can be updated (while running) to reflect changes in a Django application’s code with the menu command Kernel > Restart.'
	@echo 'HAVE FUN!'
	bash -c "${SET_VARIABLES} python manage.py shell_plus --notebook"
