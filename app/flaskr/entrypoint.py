#!/usr/bin/env python3

import os

from . import create_app
from werkzeug.debug import DebuggedApplication

app = DebuggedApplication(create_app(), evalex=False) if os.environ.get("DEBUG", False) else create_app()
