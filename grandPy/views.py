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

	parser = Parser()

	if request.method == 'POST':
		
		form = request.form
		question = form['userText']

		keyword = parser.parser(question)


		place = Place(keyword)

		place.collect_informations()

		place.collect_longitude_and_latitude(app.config['API_KEY'])
		

		answer = {'placeName' : place.name, 'informations' : place.informations, 'longitude': place.longitude, 'latitude': place.latitude}

	return json.dumps(answer)