import sys

'''
	This object represents an abstraction of a possible answer
	to a question asked in the EPFLSurvival game

	It contains the actual answer as well as the changes to the 
	gauges if the user selects this answer.

'''
class Answer(object):

	answer = ""
	changes = {}
	comment = ""

	def __init__(self, answer, changes, comment):
		self.answer = answer
		self.changes = changes
		self.commment = comment