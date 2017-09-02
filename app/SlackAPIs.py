from app import app, api, Resource
from flask import request

from slackclient import SlackClient 

BOT_NAME = 'Uobot'

slack_client = SlackClient('xoxb-236316908951-Fjnqv4KZARjLgulLcpbxZ7XO')

class HelloWorld(Resource):
	def get(self):
		return {'hello' : 'world'}

	def post(self):
		# slack_client.api_call(
		#   "chat.postMessage",
		#   channel="#bot_test",
		#   text="Hello from Python! :tada:"+str(request.json)
		# )

		return request.json

class ToDo(Resource):
	def get(self):
		return 'yes'


api.add_resource(HelloWorld, '/api/v1')
api.add_resource(ToDo, '/api/v1/todo')