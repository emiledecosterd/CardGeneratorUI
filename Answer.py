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
	suite = ""

	def __init__(self, answer, changes, comment, suite):
		self.answer = answer
		self.changes = changes
		self.comment = comment
		self.suite = suite