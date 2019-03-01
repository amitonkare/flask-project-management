import os

basedir = 	os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	# python -c 'import binascii; import os; print(binascii.b2a_qp(os.urandom(16)))'
	SECRET_KEY = '=EE<f.=BB=D7=FD},Aj<=16Z=81=BC'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
	DEBUG = False

class StagingConfig(Config):
	DEVELOPMENT = True
	DEBUG = False

class DevelopmentConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
