#!/bin/sh

if [ "$FLASK_ENV" = "development" ]; then
  flask run --host=0.0.0.0 --port=80
else
  gunicorn --bind 0.0.0.0:80 "app:create_app()"
fi