FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /code

RUN apt-get update && \
    apt-get install -y \
      binutils \
      libproj-dev \
      gdal-bin \
      libsqlite3-mod-spatialite \
      # Database client for using './manage.py dbshell' etc
      #sqlite3 \
      #spatialite-bin \
      #postgresql-client \
    && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

ENTRYPOINT ["/code/docker-entrypoint.sh"]
