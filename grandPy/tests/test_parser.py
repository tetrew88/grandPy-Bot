#!/usr/bin/python3

import sys
sys.path.append(".")

from classes.parser import Parser

class Test_Parser:

		def test_parser(self):

			testing_parser = Parser()

			sentence = "bonjour grandpy connais tu l'adresse de la tour eiffel ?"
			
			print("\n\nin: " + sentence)
			filtredSentence = testing_parser.parser(sentence)

			assert filtredSentence == "tour eiffel"