#!/bin/sh

echo "Performing Django database migrations (if any)"
python manage.py migrate

# Creat a super user
python manage.py shell -c 'from scripts import createsuperuser; createsuperuser.run()'

# Execute the CMD from the Dockerfile:
exec "$@"
