import json

import sys
sys.path.append(".")
sys.path.append("..")

from flask import request

from views import ask

from classes.parser import *


class PostResponse:
	
	@staticmethod
	def json():
		results = {userText : 'hey grandpy! ou ce trouve la tour eiffel ? '}

		return results

class LocalisationResponse:
	
	@staticmethod
	def json():
		results = {
			"results":[{
				"formatted_address" : "13 rue du test",
				"geometry":{
					"location" :{
						"lat": 48.00,
						"lng": 22.00}
						}
					}]
				}

		return results



def test_ask(monkeypatch):

	def collect_method(monkeypatch):
		return 'POST'

	def post_response(*args, **kwargs):
		return PostResponse()

	def parser_response(*args, **kwargs):
		return "tour eiffel"

	def get_localisation(*args, **kwargs):
		return LocalisationResponse()

	def get_informations(*args, **kwargs):
		return "abc"

	monkeypatch.setattr(request, "method", get_informations)
	monkeypatch.setattr(request, 'form', post_response)
	monkeypatch.setattr(parser, 'parser', parser_response)
	monkeypatch.setattr(requests, "get", get_localisation)
	monkeypatch.setattr(wikipedia, "summary", get_informations)


	answer = views.ask()
	answer = json.load(answer)

	assert answer == {
		'placeName' : 'tour eiffel', 
		'address' : '13 rue du test',
		'informations' : 'abc', 
		'longitude': 22.00, 
		'latitude': 48.00}