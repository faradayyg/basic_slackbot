from flask import Flask
from flask_restful import Resource,Api
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__) 
app.config.from_object('config')
api = Api(app)
db = SQLAlchemy(app)

from app import views,SlackAPIs
