#!/usr/bin/python3

import sys

import json

from flask import Flask, render_template, request

from grandPy.classes.parser import *
from grandPy.classes.place import *

app = Flask(__name__)
app.config.from_object('config')

# main view
@app.route('/')
def index():
	return render_template('index.html')

# ask view
@app.route('/ask', methods=['POST'])
def ask():
	answer = True

	parser = Parser()

	# if the view received a question
	if request.method == 'POST':
		form = request.form
		question = form['userText']

		# parse the user's question
		keyword = parser.parser(question)

		# if a keyword was fund in user's question
		if keyword:
			# create a place class
			place = Place(keyword)

			# collect location of the place
			answer = place.collect_localisation(app.config['API_KEY'])

			# collect information about the place
			answer = place.collect_informations()
		else:
			answer = False
		
		# if the response as different to false
		if answer:
			answer = {'placeName' : place.name, 
				'address' : place.address,
				'informations' : place.informations, 
				'longitude': place.longitude, 
				'latitude': place.latitude}

	return json.dumps(answer)