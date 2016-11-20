import sys
import json

class Card(object):
	date 		= None
	period 		= None
	section 	= None
	ranges 		= None
	answers 	= None
	image 		= None
	question 	= None
	comment 	= None

	def __init__(self, 
				question, 
				answers,
				date = -1, 
				period = "", 
				section = "", 
				ranges={
							"academics" : [0, 100],
							"social" : [0, 100],
							"finances" : [0, 100],
							"health" : [0, 100]
						}, 
				image="", 
				comment=""):
					
		self.date = date
		self.period = period
		self.section = section
		self.ranges = ranges
		self.answers = answers
		self.image = image
		self.question = question
		self.comment = comment
		
	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)