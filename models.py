from app import db
import datetime


class Projects(db.Model):
	"""docstring for Projects"""
	__tablename__ 	= 'projects'
	id 				= db.Column(db.Integer, primary_key = True)
	name 			= db.Column(db.String)
	due 			= db.Column(db.DateTime)
	created_at  	= db.Column(db.DateTime, default = datetime.datetime.now())

