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
	tag			= None
	suite		= None

	def __init__(self, 
				question, 
				answers,
				ranges, 
				date = -1, 
				period = -1, 
				section = -1, 
				image="", 
				tag="",
				suite=""):
					
		self.date = date
		self.period = period
		self.section = section
		self.ranges = ranges
		self.answers = answers
		self.image = image
		self.question = question
		self.tag = tag
		self.suite = suite
		
	def toJSON(self):
		answersTemp = []
		for a in self.answers:
			if a != None:
				answersTemp.append(a)
				
		self.answers = answersTemp
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)