# -*- coding: utf-8 -*-

class BaseConfig(object):

	DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'


class TestConfig(BaseConfig):

	DEBUG = True
	TESTING = True
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory'

class DevelopmentConfig(BaseConfig):

	pass

class ProductionConfig(BaseConfig):

	DEBUG = False