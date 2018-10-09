This script can be used to create the user and the database for notepy. 

It needs 2 env files, containing the environment variables: 

- `notepy.env` - The same file generated at the root of the project, containing notepy credentials. 
- `host-postgres.env` - A file containing the credentials of the postgres host, that will host the notepy database and user.

Then, to setup the database and its' user, you must run the `setup.sh` script.

