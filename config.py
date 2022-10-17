import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))


class Config:
    LANGUAGES = ['en', 'es', 'ru']
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    YA_TRANSLATOR_KEY = os.environ.get('YA_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL') or "https://localhost:9200"
    ELASTICSEARCH_USER=os.environ.get('ELASTICSEARCH_USER')
    ELASTICSEARCH_PASS=os.environ.get('ELASTICSEARCH_PASS')
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")
    SECURITY_EMAIL_SENDER = "abisher71@gmail.com"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABESE_URL") or \
                              f"sqlite:///{os.path.join(basedir, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = ["abisher71@gmail.com"]
    POSTS_PER_PAGE = 3



class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'