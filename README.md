# notepy 

Personal notes accessible from Django Admin, with versioning and markdown support. Soon there will also be a Rest API. 

Created based on this recipe: https://github.com/tiagoprn/experiments/tree/master/django/drf_book

## Architecture

IMPORTANT: Python 3 only supported.

This is basically a CRUD, where we have notes that can have tags (or not). Due to its simplicity, I have enabled django 
admin so you can create, update, retrieve and delete notes/tags from there. 

The notes/tags are persisted on a PostgreSQL database. In the directory `docker` you will find a ready to run 
postgresql container for your convenience, with support of backup/restore of data. You are free to customize it to your
wishes.   

The django app is called `notes_api`. Inside it you will find a `Makefile` useful to do common operations, 
like applying migrations, start a shell etc. Run `make` to see all available commands. 

## How to run locally

### Install the app dependencies
- create a virtualenv
- `$ pip install -r requirements.txt`


### Create the environment variables that will feed the sample docker container and the app: 

- `$ ./generate_env.sh`  # this will generate a `notepy.env` file with the environment variables to be set. 
- `$ source notepy.env`  # to load the environment variables into the shell. 

**IMPORTANT**: 
- This has to be done MANUALLY, because on a Makefile e.g. it does not keep the context.
- If you wish to keep the file with the environment variables (if you run `generate_env.sh` again 
it will overrite its contents), you can do that encrypting this file to somewhere safe to you. :) 

### Start the postgresql container and create the database
- make sure you have `docker-compose` installed (if not, install through your distro's package manager.)
- `cd docker/postgres`
- `make setupdb` 

*NOTE: Run `make` to see the help with other useful commands.*


### Database: run the migrations and create the django admin superuser
- `$ cd notes_api`
- `$ make migrate`
- `$ make su` (this user/password are the ones you will use to login on the django admin site)


### Start the static server (to serve the django admin assets)
- `$ make process_static`
- `$ make static_server` 


### Start the app server (to serve the django app)
- `$ make run`

*NOTE: Run `make` to see the help with other useful commands.*

### Open django admin in your browser to interact with your notes: 

[django admin url](http://localhost:8000/admin)

Now you should login with the user/password you entered on `make su`. Now you can create your notes. Have fun!
