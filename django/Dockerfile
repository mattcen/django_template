FROM --platform=$BUILDPLATFORM peaceiris/mdbook:v0.4.30 AS docs

WORKDIR /book
COPY docs src
RUN mdbook build


FROM python:3.11.3-bullseye
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
VOLUME /static
VOLUME /media
VOLUME /docs
COPY . .
COPY --from=docs /book/book /built_docs

EXPOSE 8000

HEALTHCHECK --interval=10s --timeout=5s --retries=5 CMD bash -c '[[ "$(curl -L -o /dev/null -s -w "%{http_code}\n" http://localhost:8000/)" == "200" ]]'

ENTRYPOINT ["/code/docker-entrypoint.sh"]
