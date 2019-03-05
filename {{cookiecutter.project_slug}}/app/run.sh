while ! pg_isready -h database -U postgres; do
    echo "Waiting for database.."

    sleep 5
done

psql -h database -U postgres < schema.sql

gunicorn flaskr.entrypoint:app -b 0.0.0.0:8000
