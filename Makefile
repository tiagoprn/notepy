SHELL := /bin/bash  # necessary to use the source command, which is not on sh, Makefile's default shell ;)

help:
	@echo -e " make generate-env - Generate a file with the environment variables."
	@echo -e " make env          - Load the environment variables."
	@echo -e " make listenvs     - List all environment variables."

generate-env:
	bash generate_env.sh

env: generate-env
	set -a # turn on automatic export variables from now on 
	source notepy.env
	set +a # turn off automatic export variables from now on

listenvs: env
	printenv | sort
