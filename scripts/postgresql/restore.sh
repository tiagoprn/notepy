#!/bin/bash
BACKUPS_ROOT="/backups"

source ../../notepy.env
source host-postgres.env 

##### FULL DATABASE #####
PGPASSWORD="$PGPASSWORD" pg_restore --host $POSTGRES_HOST --port $POSTGRES_PORT --username $POSTGRES_USER --dbname $POSTGRES_DB --clean --role $POSTGRES_USER -W --jobs 1 --verbose $BACKUPS_ROOT/$POSTGRES_DB.c.backup
