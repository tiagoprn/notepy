help:
	@echo 'create_migrations: create new migrations'
	@echo 'migrate: apply migrations'
	@echo 'versionate: create a initial version for all remaining models. It should be run each time you add a model to version control (django-revision)'
	@echo 'su: create superuser (user used to login to the admin and to the API)'
	@echo 'process_static: this will copy the django-admin/drf console static files to /static'
	@echo "static_server: this will run python's http server to serve the static files"
	@echo 'run: run the app'

create_migrations:
	python manage.py makemigrations notes

migrate:
	python manage.py migrate

versionate:
	python manage.py createinitialrevisions

su: migrate
	python manage.py createsuperuser

process_static:
	python manage.py collectstatic
	
static_server:	
	cd static && python -m http.server 8088 & 
	
run: migrate	
	python manage.py runserver

