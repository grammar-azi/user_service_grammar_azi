#!/bin/sh

echo "🛠 Making migrations for all apps..."
python manage.py makemigrations

echo "🛠 Resetting migrations for users app (fake zero)..."
python manage.py migrate --fake users zero

echo "🛠 Applying all migrations..."
python manage.py migrate --noinput

echo "👤 Creating superuser if not exists..."
python create_superuser.py

echo "🚀 Starting Celery worker in background..."
celery -A auth_service worker --loglevel=info &

echo "🌐 Starting Django server..."
python manage.py runserver 0.0.0.0:8000
