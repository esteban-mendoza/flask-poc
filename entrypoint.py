#!/usr/bin/env python3

import os
import subprocess

if os.getenv("FLASK_ENV") == "development":
    subprocess.run(["flask", "run", "--host=0.0.0.0", "--port=80"])
else:
    subprocess.run(["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"])
