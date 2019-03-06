#!/usr/bin/env python3

try:
    import {{cookiecutter.project_slug}}
except ImportError:
    raise RuntimeError("Couldn't import flaskr, have you run pip install -e app?")

if __name__ == "__main__":
    {{cookiecutter.project_slug}}.app.run(host="0.0.0.0", port=4141, debug=True, use_evalex=False)
