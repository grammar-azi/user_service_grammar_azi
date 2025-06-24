FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY ./auth_service /app

EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate --noinput && python create_superuser.py && python manage.py runserver 0.0.0.0:8000"]
