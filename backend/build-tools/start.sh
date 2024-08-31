echo "Waiting for postgres..."
until python3 manage.py dbshell < /dev/null; do
  echo "Waiting for database to be ready..."
  sleep 2
done

echo "PostgreSQL started"
echo "makemigrations"
python3 manage.py makemigrations
echo "migrating ..."
python3 manage.py migrate
echo "Running $@"
exec "$@"