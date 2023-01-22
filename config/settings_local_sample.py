from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Djangoの秘密キー
SECRET_KEY = ""

# DB接続情報
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# その他の変数を使用する場合
# XXXのキー
XXX = ""
