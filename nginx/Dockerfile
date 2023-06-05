FROM nginx:1.25.0-bullseye

COPY default.conf /etc/nginx/conf.d/default.conf
COPY docker-entrypoint-99-set-app-host.sh /docker-entrypoint.d/99-set-app-host.sh

HEALTHCHECK --interval=10s --timeout=5s --retries=5 CMD bash -c '[[ "$(curl -L -o /dev/null -s -w "%{http_code}\n" http://localhost/.nginx_healthcheck)" == "200" ]]'
