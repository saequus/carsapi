""" Production Settings """
import dj_database_url

from .dev import *

############
# DATABASE #
############

DATABASES = {"default": dj_database_url.parse(os.getenv("DATABASE_URL"))}


############
# SECURITY #
############

DEBUG = bool(os.getenv("DJANGO_DEBUG", False))
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", SECRET_KEY)
ALLOWED_HOSTS = ["3ckster.com", "www.3ckster.com", "localhost", "127.0.0.1"]
