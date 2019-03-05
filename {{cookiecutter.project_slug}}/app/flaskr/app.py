#!/usr/bin/env python3

import os
import secrets
import sys

from flask import Flask
from sqlalchemy import create_engine


class ConfigClass(object):
    try:
        DEBUG = bool(os.environ.get("DEBUG", False))
        SECRET_KEY = os.environ.get("SECRET_KEY", secrets.token_bytes(16))
        FLAG = os.environ["FLAG"]
        FLAG_SECRET = os.environ["FLAG_SECRET"]
        TITLE = "{{cookiecutter.project_full_name}}"
        NAVBAR = []
        LOGIN_FORM = bool("{{cookiecutter.has_login}}")
        THEME = "{{cookiecutter.theme}}"
        STATIC_URL_PATH = "/static"
        DB_CONNECTION_STRING = os.environ["DB_CONNECTION_STRING"]
    except KeyError as e:
        print(f"Flask startup failed, missing environment variable {e}", file=sys.stderr)
        sys.exit(1)


def register_models(app):
    from . import models


def register_blueprints(app):
    from .basic import app as basic_bp

    app.register_blueprint(basic_bp)


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__ + ".ConfigClass")

    register_models(app)
    register_blueprints(app)

    # setup our database connection
    app.db = create_engine(app.config["DB_CONNECTION_STRING"])

    return app
