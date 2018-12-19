# -*- coding: utf-8 -*-

class BaseConfig(object):

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory'

