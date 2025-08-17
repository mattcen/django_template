FROM --platform=$BUILDPLATFORM peaceiris/mdbook:v0.4.40 AS docs

WORKDIR /book
COPY docs src
RUN mdbook build


FROM python:3.13.7-trixie
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /code

RUN useradd django
RUN chown django:django /code

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

COPY requirements.txt /
RUN pip install -r /requirements.txt
VOLUME /media
COPY --chown=django:django . .

RUN mkdir /static
RUN chown django:django /static /media
USER django

RUN sh -c 'eval "$(cat .env.build)"; python manage.py collectstatic --no-input --clear'
COPY --chown=django:django --from=docs /book/book /static/docs

EXPOSE 8000

HEALTHCHECK --interval=10s --timeout=5s --retries=5 CMD bash -c '[[ "$(curl -L -o /dev/null -s -w "%{http_code}\n" http://localhost:8000/)" == "200" ]]'

ENTRYPOINT ["/code/docker-entrypoint.sh"]
