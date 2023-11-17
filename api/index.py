from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
	
@app.route('/ion')
def ion():
    return '宜蘭大學您好....'