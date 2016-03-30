# -*- coding: utf-8 -*-

from .base import *  # noqa

# SITE CONFIGURATION
# Hosts/domain names that are valid for this site.
# "*" matches anything, ".example.com" matches example.com and all subdomains
# See https://docs.djangoproject.com/en/stable/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += ("gunicorn", )

# If your Django app is behind a proxy that sets a header to specify secure
# connections, AND that proxy ensures that user-submitted headers with the
# same name are ignored (so that people can't spoof it), set this value to
# a tuple of (header_name, header_value). For any requests that come in with
# that header/value, request.is_secure() will return True.
# WARNING! Only set this if you fully understand what you're doing. Otherwise,
# you may be opening yourself up to a security risk.
# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#  SECURITY
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/stable/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANO_SECRET_KEY not in os.environ
SECRET_KEY = env("DJANGO_SECRET_KEY")

# if SITE_SCHEME == 'https':
#     # set this to 60 seconds and then to 518400 when you can prove it works
#     SECURE_HSTS_SECONDS = env.int('DJANGO_SECURE_HSTS_SECONDS', default=60)
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#     SECURE_SSL_REDIRECT = True
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True

# EMAIL
# ------------------------------------------------------------------------------
# DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL',
#                          default='AskCoding <Karambir <karambir@codesters.org>>')
# EMAIL_HOST = env("EMAIL_HOST")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_PORT = env.int("EMAIL_PORT", default=587)
# EMAIL_SUBJECT_PREFIX = env("EMAIL_SUBJECT_PREFIX", default='[AskCoding] ')
# EMAIL_USE_TLS = True
# SERVER_EMAIL = EMAIL_HOST_USER

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES['default'].update(env.db("DATABASE_URL"))  # Should not override all db settings


# TEMPLATE CONFIGURATION
# -----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/stable/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
]
