from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/ask', methods = ['post'])
def ask():
	form = request.form

	question = form['userText']

	
