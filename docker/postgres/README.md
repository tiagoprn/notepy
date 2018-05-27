- The container is called `postgres_notepy`. Edit it to your wish. 

- `utils/` contains scripts to dump and restore the database, with some
  environment variables hardcoded there also.

- `postgres.env` contains the credentials to create the database. Here is a
  sample of its full-blown contents:

```
# Environment variables for postgresql.
POSTGRES_USER=notepy
PGPASSWORD=12345678
POSTGRES_DB=notepy
TZ=Etc/UTC
```

- According to
  https://stackoverflow.com/questions/19674456/run-postgresql-queries-from-the-command-line,
if you set the enviroment variable PGPASSWORD you do not need to inform your
password.

