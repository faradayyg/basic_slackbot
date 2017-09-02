# import os
from slackclient import SlackClient 

BOT_NAME = 'Uobot'

slack_client = SlackClient('xoxb-236316908951-Fjnqv4KZARjLgulLcpbxZ7XO')

if __name__ == "__main__":
    slack_client.api_call(
      "chat.postMessage",
      channel="#wakaapp",
      text="Hello from Python! :tada:"
    )
        
          