from app import app, api, Resource, handlers
from flask import request

from slackclient import SlackClient 

BOT_NAME = 'Uobot'

slack_client = SlackClient('xoxb-236316908951-Fjnqv4KZARjLgulLcpbxZ7XO')

class HelloWorld(Resource):
	def get(self):
		return {'hello' : 'world'}

	def post(self):

		event = request.json['event']
		if event['type'] == 'message':
			if event['text'].find("@uobot") > -1:
				channel_info = slack_client.api_call("channels.info", channel=event['channel'])
				if event['text'].find("show") > -1 or event['text'].find("list") > -1\
				or event['text'].find("display") > -1 and event['text'].find("project") > -1:

					# user_info = slack_client.api_call("users.profile.get", user=event['user'])
					# return user_info
					

					slack_client.api_call(
					  "chat.postMessage",
					  channel="#"+channel_info['channel']['name_normalized'],
					  text= handlers.list_projects()
					)
					return request.json['event']

				if event['text'].find("add") > -1 or event['text'].find("create") > -1\
				 and event['text'].find("project") > -1:
				 	if handlers.create_project(event['text']) == 'nan':
				 		pass
				 	else:
				 		slack_client.api_call(
						  "chat.postEphemeral",
						  channel="#"+channel_info['channel']['name_normalized'],
						  text= "Project was successfully created",
						  user = event['user']
						)

				if event['text'].find("remove") > -1 or event['text'].find("delete") > -1\
				 and event['text'].find("project") > -1:
				 	handlers.delete_project(event['text'])
				 	slack_client.api_call(
						  "chat.postEphemeral",
						  channel="#"+channel_info['channel']['name_normalized'],
						  text= "Project was successfully deleted",
						  user = event['user']
						)

				else:
					slack_client.api_call(
						  "chat.postMessage",
						  channel="#"+channel_info['channel']['name_normalized'],
						  text= "Hi there :smile: I am Uobot, a friendly chatbot \n you can ask me to do stuff like: \n *list all projects* \n _or_  \n *create a project {project name}*"
						)




		return request.json['event']

class ToDo(Resource):
	def get(self):
		return 'yes'


api.add_resource(HelloWorld, '/api/v1')
api.add_resource(ToDo, '/api/v1/todo')