#!/usr/bin/env python3

try:
    from flaskr import create_app
except ImportError:
    raise RuntimeError("Couldn't import flaskr, have you run pip install -e app?")

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4141, debug=True, use_evalex=False)
