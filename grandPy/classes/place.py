#!/usr/bin/python3

import requests
import wikipedia

import re

class Place():

	def __init__(self, name):
		self.name = name

		self.address = False
		
		self.informations = False

		self.longitude = False
		self.latitude = False

		self.recommandationList = False

	
	def collect_informations(self):

		"""
			wikiRequest = requests.Session()

			URL = "https://fr.wikipedia.org/w/api.php"

			SEARCHPAGE = self.informations

			PARAMS = {"action": "query",
			"format": "json",
			"list": "search",
			"srsearch": self.name}

			response = wikiRequest.get(url=URL, params=PARAMS)
			data = response.json()

			self.informations = data["query"]["search"][0]["snippet"]

			self.informations = re.sub('<[^<]+?>', '', self.informations)
		"""

		try:
			wikipedia.set_lang("fr")

			self.informations = wikipedia.summary(self.name, sentences = 1)
		
		except:
			return False

		return True


	def collect_localisation(self, apiKey):
		"""https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}"""
		

		url = ('https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}'
           .format(self.name, apiKey))

		try:
			response = requests.get(url)

			print(response)

			response = response.json()

			print(response)

			response = response['results'][0]

			self.address = response["formatted_address"]

			localisation = response['geometry']['location']

			self.longitude = localisation['lat']
			self.latitude = localisation['lng']

		except:
			print("22222222")
			return False


		return True