from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Project(db.Model):
	__tablename__ = 'projects'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String())
	client = db.Column(db.String())
	technology = db.Column(db.String())
	status = db.Column(db.String())

	def __init__(self, name, client, technology, status):
		self.name = name
		self.client = client
		self.technology = technology
		self.status = status
	
	def __repr__(self):
		return '<Project {}>'.format(self.id)

	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'client': self.client,
			'technology': self.technology,
			'status': self.status
		}

class Task(db.Model):
	__tablename__ = 'tasks'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	description = db.Column(db.Text, nullable=False)
	created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
	project = db.relationship('Project', backref=db.backref('projects', lazy=True))

	def __repr__(self):
		return '<Task {}>'.format(self.id)