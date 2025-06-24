#!/bin/sh

echo "✅ Migrating database..."
python manage.py migrate --noinput

echo "✅ Collecting static files..."
python manage.py collectstatic --noinput

echo "🚀 Starting Gunicorn..."
gunicorn auth_service.wsgi:application --bind 0.0.0.0:8000
