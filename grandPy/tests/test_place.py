#!/usr/bin/python3

import sys
sys.path.append(".")

import pytest
import requests
import json

from classes.place import Place
from io import BytesIO


class Test_place:
	
	def test_collect_informations(self):
		place = Place("Saint-Dié-Des-Vosges")

		place.collect_informations()

		assert type(place.informations) == str


	def test_collect_localisation(monkeypatch):
		place = Place('Paris')

		results = [{
			"results":[{
				"formatted_address" : "13 rue du test",
				"geometry":{
					"location" :{
						"lat": 48.00,
						"lng": 22.00
						}
					}
				}]
			}]

		def mockreturn(request):
			return BytesIO(json.dumps(results).encode())

			monkeypatch.setattr(request, 'get' , mockreturn)

		place.collect_localisation("")
		assert place.address == "14 rue du test"
