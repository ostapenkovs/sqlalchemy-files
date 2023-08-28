#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z $FLASK_DB $POSTGRES_PORT; do
    sleep 0.1
done

echo "PostgreSQL started."

python app.py

exec "$@"