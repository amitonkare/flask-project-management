import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(os.environ['APP_SETTINGS'])
	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	# Include all models
	from flaskr.db import init_db
	init_db()
	
	from flaskr.models import db
	db.init_app(app)
	
	# db.create_all()

	from flask_migrate import Migrate
	migrate = Migrate(app, db)

	# Include all routes
	from . import routes
	app.register_blueprint(routes.home)
	app.register_blueprint(routes.project)

	def list_routes():
		return ['%s' % rule for rule in app.url_map.iter_rules()]
	print("Available Routes: ", list_routes())

	return app
