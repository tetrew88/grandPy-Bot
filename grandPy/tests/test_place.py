#!/usr/bin/python3

import sys
sys.path.append(".")

import wikipedia
import requests
import json

from classes.place import Place


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


def test_collect_informations(monkeypatch):
	testPlace = Place("paris")

	def get_informations(*args, **kwargs):
		return "abc"

	monkeypatch.setattr(wikipedia, "summary", get_informations)

	testPlace.collect_informations()
	assert testPlace.informations == "abc"


def test_collect_localisation(monkeypatch):
	testPlace = Place("paris")

	def get_localisation(*args, **kwargs):
		return LocalisationResponse()

	monkeypatch.setattr(requests, "get", get_localisation)

	testPlace.collect_localisation("fakeApiKey")

	assert testPlace.address == "13 rue du test"