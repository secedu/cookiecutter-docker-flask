# {{cookiecutter.project_full_name}}

This is a cookiecutter template for creating a standard COMP6443 challenge.

## Design/Specification

Fill me in with details about the challenge.

## Usage

### Dev

*Note: These are general usage instructions.*

```bash
pipenv install -d # Enables dev dependencies (linter, etc) 
pipenv shell

# In the pipenv shell

pip install -e app # Installs flaskr as a editable application

FLAG=FLAG{SAMPLE_FLAG} FLAG_SECRET=SECRET DB_CONNECTION_STRING=postgresql://user:pass@host/database python run.py
```
