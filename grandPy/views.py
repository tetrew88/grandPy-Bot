import sys

from flask import Flask, render_template, request

from grandPy.classes.parser import *
from grandPy.classes.grandPy import *

app = Flask(__name__)

apiKey = 'AIzaSyD3UanyjV5IphscC92cuW9Kx9R-FzVMyco'

answerDict = {"information":False, "adress":False, "map":False}

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/ask', methods = ['POST'])
def ask():

	parser = Parser()
	grandPy = GrandPy()

	if request.method == 'POST':
		
		form = request.form
		question = form['userText']


		question = parser.parser(question)

		answerDict["information"] = grandPy.collect_informations(question)

		print(answerDict["information"])

	return answerDict


@app.route('/answer', methods = ['GET'])
def answer():
	pass