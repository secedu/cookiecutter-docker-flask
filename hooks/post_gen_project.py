#!/usr/bin/env python3

import logging
import os

logger = logging.getLogger(__name__)

project_root = os.getcwd()

logger.info("Creating config symlink")

# Nuke the existing file if it exists
if os.path.isfile("config.py"):
    os.unlink("config.py")

os.symlink("app/config.py", "config.py")
