#!/bin/sh

echo "🛠 Applying migrations..."
python manage.py migrate --noinput

echo "👤 Creating superuser if not exists..."
python -c "
from django.contrib.auth import get_user_model
User = get_user_model()
email = 'admin@example.com'
username = 'admin'
password = 'your_secure_password'
if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(email=email, username=username, password=password)
    print('Superuser created.')
else:
    print('Superuser already exists.')
"

echo "🚀 Starting Celery worker in background..."
celery -A auth_service worker --loglevel=info &

echo "🌐 Starting Django server..."
python manage.py runserver 0.0.0.0:8000
