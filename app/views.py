from app import app

@app.route('/')
def home():
	return "Oh yeah, I am home"