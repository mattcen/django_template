# Dockerised Django

This is a Dockerised Django Project template

## Getting started

1. Clone this repo, cd into it, and copy the `.env` file:

```sh
git clone https://github.com/user/repo
cd repo
cp .env.example .env
```

2. Edit the `.env` file and review its settings. At a minimum, you'll probably want to uncomment `DEBUG=true` for testing

3. Start Django

  * To do so using Docker:

    ```sh
    docker-compose up -f docker-compose.dev.yml -d
    ```

  * To do so using a Python `venv`:

    NOTE: These instructions are only tested on macOS and Linux

    Perform the initial set-up (do this only once):

    ```sh
    # Create a virtual environment
    python3 -m venv .venv
    # Activate virtual environment
    . .venv/bin/activate
    # Install Python dependencies
    pip install -r django/requirements.txt
    # Change to the django dir
    cd django/
    # Run the Docker entrypoint script to set up an initial superuser etc
    ./docker-entrypoint.sh
    cd ..
    deactivate
    ```

    Start up Django (do this every time):

    ```
    # Activate virtual environment
    . .venv/bin/activate
    # Change to the django dir
    cd django/
    # Start Django
    ./manage.py runserver
    ```

4. Log into admin console at http://localhost:8000/admin as `root`/`root`

## Notes

By default there is no `docker-compose.yml`, so `docker-compose up` won't work without specifying one of the other files.

`docker-compose.dev.yml` is designed for use during development. You probably also want to uncomment the `DEBUG` line in the `.env` file in this case.

`docker-compose.prod.yml` is designed for production.

`docker-compose.traefik.yml` is designed for production when using Traefik as a HTTP proxy

For convenience, any of these files could be copied or symlinked to `docker-compose.yml` so you don't need to specify the file with `docker-compose -f file.yml`.
