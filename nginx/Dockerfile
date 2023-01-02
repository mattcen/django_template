FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY django.conf /etc/nginx/conf.d

HEALTHCHECK --interval=10s --timeout=5s --retries=5 CMD bash -c '[[ "$(curl -L -o /dev/null -s -w "%{http_code}\n" http://localhost/.nginx_healthcheck)" == "200" ]]'
