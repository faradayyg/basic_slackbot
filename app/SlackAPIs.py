from app import app, api, Resource
from flask import request


class HelloWorld(Resource):
	def get(self):
		return {'hello' : 'world'}

	def post(self):
		return request.json

class ToDo(Resource):
	def get(self):
		return 'yes'


api.add_resource(HelloWorld, '/api/v1')
api.add_resource(ToDo, '/api/v1/todo')