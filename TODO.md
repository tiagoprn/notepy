- Change django admin url from /admin to another one.
- Make a test importing the contents of my dokuwiki, with old versions of all the documents (create a jupyter notebook to accompany this process.)
- freeze the requirements
- Dockerize the app, create a docker compose changing the database to postgres (the docker compose file was already created.)

- Find a way to run this SQL statements on the postgresql database: 
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

- Deploy on DigitalOcean on a new postgres dedicated instance, supporting docker volumes for easy backup - and use HTTPS on the admin site.
