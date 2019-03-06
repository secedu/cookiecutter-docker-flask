#!/usr/bin/env python3

try:
    from {{cookiecutter.project_slug}} import app
except ImportError:
    raise RuntimeError("Couldn't import {{cookiecutter.project_slug}}, have you run pip install -e app?")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4141, debug=True, use_evalex=False)
