from os import environ
from pathlib import Path
from decouple import config

from google.oauth2 import service_account


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE"),
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}


DOMAIN = config("DOMAIN")

SITE_NAME = config("SITE_NAME")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    BASE_DIR / "serviceaccount.json"
)
GS_BUCKET_NAME = config("GS_BUCKET_NAME")
GS_DEFAULT_ACL = "publicRead"
