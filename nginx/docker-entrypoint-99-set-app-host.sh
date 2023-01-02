#!/bin/sh

if [ -n "$WEB_APP_HOST" ]
then
  sed -i "s/replace_this_with_web_app_hostname_and_port/$WEB_APP_HOST/g" /etc/nginx/conf.d/default.conf
fi
