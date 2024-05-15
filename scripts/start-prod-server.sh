#!/bin/sh
gunicorn dms.wsgi --bind 0.0.0.0:8000 --timeout 60 --access-logfile - --error-logfile -
