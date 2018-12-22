# -*- coding: utf-8 -*-

class BaseConfig(object):

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RECAPTCHA_PUBLIC_KEY = '6LchGYMUAAAAAJMGrh4j9Dd8MSVOY3VTsYLHq-SC'
    RECAPTCHA_PRIVATE_KEY = '6LchGYMUAAAAAKq_gfyY_B_NnFLnx_ufMb9AJo9h'
    ADMIN = 'tthiaguinho638@gmail.com'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'tthiaguinho638@gmail.com'
    MAIL_PASSWORD = '654750321529456'


class DevelopmentConfig(BaseConfig):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory'

