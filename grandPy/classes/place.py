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
		"""method for collect information about the place"""

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
			# set language to wikipedia library
			wikipedia.set_lang("fr")

			#collect 1 sentence of information about the place
			self.informations = wikipedia.summary(self.name, sentences = 1)
		
		except:
			return False

		return True


	def collect_localisation(self, apiKey):
		"""method for collect localisation of the class"""

		# query url
		url = ('https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}'
           .format(self.name, apiKey))

		try:
			# do request to url
			response = requests.get(url)

			# received response and convert her
			response = response.json()

			# collect localisation and adress from response
			response = response['results'][0]

			self.address = response["formatted_address"]

			localisation = response['geometry']['location']

			self.longitude = localisation['lat']
			self.latitude = localisation['lng']

		except:
			return False


		return True