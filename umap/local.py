# -*- coding:utf-8 -*-

"""
Example settings for local development

Use this file as a base for your local development settings and copy
it to umap/settings/local.py. It should not be checked into
your code repository.

"""

from umap.settings.base import *   # pylint: disable=W0614,W0401
from email.utils import getaddresses

import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    TIME_ZONE=(str, 'UTC'),
)

SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')

DEBUG = env('DEBUG')

ADMINS = getaddresses([env('UMAP_ADMINS', default='You <your@email.example.net>,Me <my@email.example.com>')])

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST': env("POSTGRES_HOST", default="localhost"),
        'PORT': env("POSTGRES_PORT", default="5432"),
    }
}

COMPRESS_ENABLED = False
COMPRESS_OFFLINE = True

LANGUAGE_CODE = env('UMAP_LANGUAGE_CODE', default='en')

# Set to False if login into django account should not be possible. You can
# administer accounts in the admin interface.
ENABLE_ACCOUNT_LOGIN = env('UMAP_ENABLE_ACCOUNT_LOGIN', default=True)

# Start with no auth backends, and add social auth backends if their env vars are set.
AUTHENTICATION_BACKENDS = ()

SOCIAL_AUTH_GITHUB_KEY = env('UMAP_SOCIAL_AUTH_GITHUB_KEY', default=None)
SOCIAL_AUTH_GITHUB_SECRET = env('UMAP_SOCIAL_AUTH_GITHUB_SECRET', default=None)
if SOCIAL_AUTH_GITHUB_KEY and SOCIAL_AUTH_GITHUB_SECRET:
    AUTHENTICATION_BACKENDS += ('social_core.backends.github.GithubOAuth2',)

SOCIAL_AUTH_BITBUCKET_KEY = env('UMAP_SOCIAL_AUTH_BITBUCKET_KEY', default=None)
SOCIAL_AUTH_BITBUCKET_SECRET = env('UMAP_SOCIAL_AUTH_BITBUCKET_SECRET', default=None)
if SOCIAL_AUTH_BITBUCKET_KEY and SOCIAL_AUTH_BITBUCKET_SECRET:
    AUTHENTICATION_BACKENDS += ('social_core.backends.bitbucket.BitbucketOAuth',)

# We need email to associate with other Oauth providers
SOCIAL_AUTH_GITHUB_SCOPE = ["user:email", ]

SOCIAL_AUTH_TWITTER_KEY = env('UMAP_SOCIAL_AUTH_TWITTER_KEY', default=None)
SOCIAL_AUTH_TWITTER_SECRET = env('UMAP_SOCIAL_AUTH_TWITTER_SECRET', default=None)
if SOCIAL_AUTH_TWITTER_KEY and SOCIAL_AUTH_TWITTER_SECRET:
    AUTHENTICATION_BACKENDS += ('social_core.backends.twitter.TwitterOAuth',)

SOCIAL_AUTH_OPENSTREETMAP_KEY = env('UMAP_SOCIAL_AUTH_OPENSTREETMAP_KEY', default=None)
SOCIAL_AUTH_OPENSTREETMAP_SECRET = env('UMAP_SOCIAL_AUTH_OPENSTREETMAP_SECRET', default=None)
if SOCIAL_AUTH_OPENSTREETMAP_KEY and SOCIAL_AUTH_OPENSTREETMAP_SECRET:
    AUTHENTICATION_BACKENDS += ('social_core.backends.openstreetmap.OpenStreetMapOAuth',)

# Finally, fall back on the default Django backend
AUTHENTICATION_BACKENDS += ('django.contrib.auth.backends.ModelBackend',)

MIDDLEWARE += (
    'social_django.middleware.SocialAuthExceptionMiddleware',
)
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_BACKEND_ERROR_URL = "/"

# If you want to add a playgroud map, add its primary key
# UMAP_DEMO_PK = 204
# If you want to add a showcase map on the home page, add its primary key
# UMAP_SHOWCASE_PK = 1156
# Add a baner to warn people this instance is not production ready.
UMAP_DEMO_SITE = env('UMAP_DEMO_SITE', default=True)

# Whether to allow non authenticated people to create maps.
UMAP_ALLOW_ANONYMOUS = env('UMAP_ALLOW_ANONYMOUS', default=False)

# This setting will exclude empty maps (in fact, it will exclude all maps where
# the default center has not been updated)
UMAP_EXCLUDE_DEFAULT_MAPS = env('UMAP_EXCLUDE_DEFAULT_MAPS', default=False)

# How many maps should be showcased on the main page resp. on the user page
UMAP_MAPS_PER_PAGE = env('UMAP_MAPS_PER_PAGE', default=5)
# How many maps should be showcased on the user page, if owner
UMAP_MAPS_PER_PAGE_OWNER = env('UMAP_MAPS_PER_PAGE_OWNER', default=10)

SITE_URL = env('UMAP_SITE_URL', default='http://localhost:8019')
SHORT_SITE_URL = env('UMAP_SHORT_SITE_URL', default='http://s.hort')

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache',
#     }
# }

# POSTGIS_VERSION = (2, 1, 0)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# You need to unable accent extension before using UMAP_USE_UNACCENT
# python manage.py dbshell
# CREATE EXTENSION unaccent;
UMAP_USE_UNACCENT = False

# Put the site in readonly mode (useful for migration or any maintenance)
UMAP_READONLY = env('UMAP_READONLY', default=False)


# For static deployment
STATIC_ROOT = '/static'

# For users' statics (geojson mainly)
MEDIA_ROOT = '/media'

# Default map location for new maps
LEAFLET_LONGITUDE = env('UMAP_LEAFLET_LONGITUDE', default=2)
LEAFLET_LATITUDE = env('UMAP_LEAFLET_LATITUDE', default=51)
LEAFLET_ZOOM = env('UMAP_LEAFLET_ZOOM', default=6)

# Number of old version to keep per datalayer.
UMAP_KEEP_VERSIONS = env('UMAP_KEEP_VERSIONS', default=10)

TIME_ZONE = env("TIME_ZONE")
USE_TZ = True
