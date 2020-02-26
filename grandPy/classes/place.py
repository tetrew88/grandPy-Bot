#!/usr/bin/python3

import requests
import wikipedia


class Place():

	def __init__(self, name):
		self.name = name
		
		self.informations = ""

		self.longitude = 0
		self.latitude = 0

	
	def collect_informations(self):
		
		try:
			wikipedia.set_lang("fr")

			self.informations = wikipedia.summary(self.name, sentences = 1)
		
		except:
			self.informations = False


	def collect_longitude_and_latitude(self, apiKey):
		url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(self.name, apiKey))

		try:
			response = requests.get(url)

			response = response.json()

			localisation = response['results'][0]['geometry']['location']

			self.longitude = localisation['lat']
			self.latitude = localisation['lng']


		except:
			print("erreur lors de la récupération de la localisation")

			self.longitude = 0
			self.latitude = 0

			return False


		return True