#!/usr/bin/python3

import sys
sys.path.append(".")

from classes.grandPy import GrandPy


class Test_grandPy:
	
	def test_collect_informations(self):
		grandPy = GrandPy()

		keyword = "Saint-Dié-Des-Vosges"

		print("\n\nin: " + keyword)

		text = grandPy.collect_informations(keyword)

		print("\nOut: " + text + "\n\n")

		assert type(text) == str