import sys

# Qt classes
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Custom classes
from MainWindowGUI import Ui_MainWindow
from Answer import Answer
from AnswerDialog import AnswerDialog

'''
/!\
	MAKE GUI CLASS QWIDGET SUBCLASS!!! 
	QtWidgets.QWidget
	(otherwise signals won't work)
/!\
'''

class MainWindow(Ui_MainWindow):

	currentAnswer = None

	def __init__(self, window):

		Ui_MainWindow.__init__(self)
		self.setupUi(window)
		self.setup()
		

	def setup(self):

		# Setup connections 
		self.send_button.clicked.connect(self.on_send)
		self.show1_button.clicked.connect(lambda: self.on_showAnswer(1))
		self.show2_button.clicked.connect(lambda: self.on_showAnswer(2))
		self.show3_button.clicked.connect(lambda: self.on_showAnswer(3))
		self.show4_button.clicked.connect(lambda: self.on_showAnswer(4))

		# Desable everything with a checkbox

		# If a checkbox is checked, enable the corresponding field

		# Add a tooltip on sliders to diplay current value


	def on_showAnswer(self, tag):

		# Keep track of which answer it is
		self.currentAnswer = tag

		# Desactivate the window
		self.enabled = False

		# Show the dialog to edit the answer
		dialog = QDialog(self)
		answerDialog = AnswerDialog(dialog, self.question_lineEdit.text())
		answerDialog.completed.connect(self.updateAnswers)
		dialog.show()


	def on_send(self):

		# Verify all the fields

		# Send to Firebase


	def updateAnswers(self, answer):

		# Reactivate window
		self.enabled = True

		print('Updating answer')





