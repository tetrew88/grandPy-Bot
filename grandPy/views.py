import sys

import json

from flask import Flask, render_template, request

from grandPy.classes.parser import *
from grandPy.classes.place import *

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/ask', methods = ['POST'])
def ask():
	answer = True

	parser = Parser()

	if request.method == 'POST':
		
		form = request.form
		question = form['userText']

		keyword = parser.parser(question)

		if keyword != False:
			place = Place(keyword)

			answer = place.collect_localisation(app.config['API_KEY'])

			answer = place.collect_informations()
		else:
			answer = False
		

		if answer != False:
			answer = {'placeName' : place.name, 
			'address' : place.address,
			'informations' : place.informations, 
			'longitude': place.longitude, 
			'latitude': place.latitude}

	return json.dumps(answer)