#!/bin/sh

echo "Performing Django database migrations (if any)"
umap migrate --no-input

echo "Copying static files"
umap collectstatic --no-input --clear
umap compress

# Creat a super user
umap shell --pythonpath . -c 'from scripts import createsuperuser; createsuperuser.run()'

# Execute the CMD from the Dockerfile:
exec "$@"
