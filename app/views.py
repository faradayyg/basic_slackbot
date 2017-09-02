from app import app
from flask import request
@app.route('/api/v1', methods=['POST','GET'])
def home():
	return request.form['challenge']