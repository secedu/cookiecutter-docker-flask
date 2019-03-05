#!/usr/bin/env python3

from flaskr import create_app
app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4141, debug=True, use_evalex=False)
