#!/usr/bin/env python3

from flask import (
    request,
    render_template,
    current_app,
)
from . import bp as app   # Note that app = blueprint, current_app = flask context


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/ping")
def ping():
    return "pong"


@app.route("/flag_debug", methods=["POST"])
def flag_debug():
    if request.form.get("flag_secret", "") == current_app.config["FLAG_SECRET"]:
        return current_app.config["FLAG"]
    return ":(", 401
