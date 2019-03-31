#!/usr/bin/env python3

import json
import logging
import os
import urllib.request

logger = logging.getLogger(__name__)

project_root = os.getcwd()

logger.info("Creating config symlink")

# Nuke the existing file if it exists
if os.path.isfile("config.py"):
    os.unlink("config.py")

os.symlink("app/config.py", "config.py")

# Get the latest release of flask-core
rv = urllib.request.urlopen(
    "https://pypi.python.org/pypi/flask-core/json"
).read()

release_data = json.loads(rv)
latest_fc = release_data["info"]["version"]

# Pin Pipfile and requirements.txt to latest major
for f in ["Pipfile", "app/requirements.txt"]:
    with open(f, "r") as fd:
        contents = fd.read()

    with open(f, "w") as fd:
        fd.write(contents.replace("!FLASK_CORE_LATEST!", latest_fc))
