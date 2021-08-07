import os
import sys

import dj_database_url

SETTINGS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(SETTINGS_DIR)


if os.path.exists(os.path.join(SETTINGS_DIR, "settings/settings_local.py")):
    from .settings_local import *


SECRET_KEY = "agsWEmsD6g9d120E23vsk"
ALLOWED_HOSTS = ["*"]

#################################
# # # Application definition # # #
#################################

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.admin",
    "django.contrib.staticfiles",
    "drf_yasg",
    "src",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Add dist to
        "DIRS": ["dist"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

############
# DATABASE #
############

if len(sys.argv) >= 2 and "test" in sys.argv:
    DATABASE_URL = "postgres://slavaspetsyian@localhost:5432/test_carsapi"


DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

MIDDLEWARE_CLASSES = ()

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "dist", "static")
STATICFILES_DIRS = []


##################
# # # Static # # #
##################

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
}

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

###############################
# # # Application specific # # #
###############################

DOT_GOV_URL = "https://vpic.nhtsa.dot.gov/api/"
MODELS_FOR_MAKE_API_URL = "vehicles/getmodelsformake/"
JSON_FORMAT = "format=json"
RESPONSE_RETURNED_SUCCESSFULLY = "Response returned successfully"
