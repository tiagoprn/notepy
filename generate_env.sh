#!/bin/bash
cat << EOF > notepy.env
# Environment variables for notepy.
NOTEPY_SECRET_KEY=$(./random_password --num_chars 50)
POSTGRES_USER=notepy
POSTGRES_DB=notepy
PGPASSWORD=$(./random_password --num_chars 10)  # This variable name for the pg password is for convenience on psql
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
TZ=Etc/UTC
EOF
