FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

RUN apt-get update && \
    apt-get install -y \
      binutils \
      libproj-dev \
      gdal-bin \
      libsqlite3-mod-spatialite \
      # Database client for using './manage.py dbshell' etc
      sqlite3 \
      spatialite-bin \
      postgresql-client \
    && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*
