#!/usr/bin/python3

import wikipedia

class GrandPy():
	def __init__(self):
		pass

	def collect_informations(self, keyword):
	
		try:
			wikipedia.set_lang("fr")

			text = wikipedia.summary(keyword, sentences=1)
		
		except:
			return False

		return text


	def collect_adress(self, keyword):
		pass


	def collect_map(self, keyword):
		pass