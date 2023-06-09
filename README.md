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

    ```sh
    # Activate virtual environment
    . .venv/bin/activate
    # Change to the django dir
    cd django/
    # Start Django
    ./manage.py runserver
    ```

4. Log into admin console at http://localhost:8000/admin as `root`/`root`

## Creating your first app

Now you've got Django up and running, you should be at the point where you can follow the [Django documentation](https://docs.djangoproject.com/en/dev/intro/tutorial01/#creating-the-polls-app) to create your first app. The short version of what you need to do from here is:

1. Create an app:

  If using Docker:

  ```sh
  docker-compose exec app ./manage.py startapp myapp
  ```
  If using a virtual environment:

  ```sh
  ./manage.py startapp myapp
  ```

2. Edit both `django/myproject/settings.py` and `django/myproject/urls.py`,
   search for `myapp`, and uncomment the line as instructed.

3. Set up appropriate views in `django/myapp/views.py`, and URLs in `django/myapp/urls.py`, before browsing to http://localhost:8000/

## Notes

By default there is no `docker-compose.yml`, so `docker-compose up` won't work without specifying one of the other files.

`docker-compose.dev.yml` is designed for use during development. You probably also want to uncomment the `DEBUG` line in the `.env` file in this case.

`docker-compose.prod.yml` is designed for production.

`docker-compose.traefik.yml` is designed for production when using Traefik as a HTTP proxy

For convenience, any of these files could be copied or symlinked to `docker-compose.yml` so you don't need to specify the file with `docker-compose -f file.yml`.
