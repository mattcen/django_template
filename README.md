# Dockerised Django

This is a Dockerised Django Project template

## Getting started

1. Clone this repo, cd into it, and copy the `.env` file:

```sh
git clone https://github.com/user/repo
cd repo
cp .env.example .env
```

2. Start up the Docker environment:

```
docker-compose up -f docker-compose.dev.yml -d
```

3. Log into admin console at http://localhost:8000/admin as `root`/`root`.

## Notes

By default there is no `docker-compose.yml`, so `docker-compose up` won't work without specifying one of the other files.

`docker-compose.dev.yml` is designed for use during development. You probably also want to uncomment the `DEBUG` line in the `.env` file in this case.

`docker-compose.prod.yml` is designed for production.

For convenience, either of these files could be copied to `docker-compose.yml` so you don't need to specify the file with `docker-compose -f file.yml`.
