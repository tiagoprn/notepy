SHELL := /bin/bash  # necessary to use the source command, which is not on sh, Makefile's default shell ;)

help:
	@echo -e " make bash         - Run a bash session."
	@echo -e " make psql         - Log on the postgresql instance on psql."
	@echo -e " make backup       - Make a backup of postgresql data."
	@echo -e " make restore      - Restore to the most recent database backup."
	@echo -e " make stop         - Stop the container."
	@echo -e " make remove       - CAUTION: Remove (delete) the container and the PG_DATA container (the BACKUPS volume will remain)."
	@echo -e " make start        - Start the container."
	@echo -e " make setupdb      - Setup database credentials and default encoding to be ready for a django app."

bash:
	docker exec -it $$(docker ps | grep postgres | awk '{print $$1}') bash

psql:
	docker exec -it $$(docker ps | grep postgres | awk '{print $$1}') psql -U notepy notepy

backup:
	docker exec -i $$(docker ps | grep postgres | awk '{print $$1}') /utils/dump.sh

restore:
	docker exec -i $$(docker ps | grep postgres | awk '{print $$1}') /utils/restore.sh

stop: 
	sudo docker-compose stop 

remove: backup stop
	sudo docker-compose rm -f
	sudo docker volume rm postgres_PG_NOTEPY_DATA

start: 
	sudo docker-compose up -d
	@echo -e "IMPORTANT: If this is the first time you start this container, run: \n    $ make setupdb"

setupdb: start
	docker exec -i $$(docker ps | grep postgres | awk '{print $$1}') /utils/setup.sh
