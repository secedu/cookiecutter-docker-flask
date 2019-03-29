# {{cookiecutter.project_full_name}}

This is a cookiecutter template for creating a standard COMP6443 challenge.

## Design/Specification

Fill me in with details about the challenge.

## Usage

*Note: These are general usage instructions.*

Until docker-compose properly introduces `--env-file` support so that the compose stack itself accepts envvars defined there, you must define
the following envvars within your environment:

- INFRA_PGPASSWORD
    - Used for populating the database 
- PUBLISH_PORT
    - Which external port to publish the application on

### Prod

```bash
export INFRA_PGPASSWORD=a_sample_psql_password
export PUBLISH_PORT=8000

# If you wish to provide your own envvar file, defaults to reading .prod.env
export ENV_FILE=.prod.env

docker-compose build

docker-compose up -d
```

### Dev

```bash
pipenv install -d --pre # Enables dev dependencies (linter, etc) 
pipenv shell

# In the pipenv shell

pip install -e app  # Installs {{cookiecutter.project_full_name}} as a editable application

source .dev.env  # Update this appropriately

python run.py
```
