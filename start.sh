#!/usr/bin/env bash
set -o errexit

mkdir -p "${MEDIA_ROOT:-/var/data/media}"
python manage.py migrate
exec gunicorn personal_site.wsgi:application --bind 0.0.0.0:"${PORT:-8000}"

