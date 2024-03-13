#!/bin/bash
set -eEu -o pipefail

pip3 install --user -r django/requirements.txt;
git submodule init;
git submodule update;
! [ -e .env ] &&
    sed '/^\(XERO_API_CLIENT_ID\|SCOUTSVIC_API_KEY\)/s/^/#/;/[=#]DEBUG/s/^#//' .env.example > .env;
./django/manage.py migrate
