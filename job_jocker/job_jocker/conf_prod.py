import os
from .settings import *
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = False
DATABASES = {
"default": {
"ENGINE": "django.db.backends.postgresql_psycopg2",
"NAME": "Job_jocker",
"USER": "django",
"PASSWORD": "geekbrains",
"HOST": "127.0.0.1",
"PORT": "5432",
}
}
del STATICFILES_DIRS
STATIC_ROOT = BASE_DIR / "static"