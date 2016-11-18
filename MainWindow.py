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
		self.dateEdit.setEnabled(False)
		self.period_comboBox.setEnabled(False)
		self.section_comboBox.setEnabled(False)
		self.imageName_lineEdit.setEnabled(False)
		self.show1_button.setEnabled(False)
		self.show2_button.setEnabled(False)
		self.show3_button.setEnabled(False)
		self.show4_button.setEnabled(False)

		print('Setup')

		# If a checkbox is checked, enable the corresponding field
		self.date_checkBox.stateChanged.connect(
			lambda: self.toggleEnabled(self.dateEdit))
		self.period_checkBox.stateChanged.connect(
			lambda: self.toggleEnabled(self.period_comboBox))
		self.section_checkBox.stateChanged.connect(
			lambda: self.toggleEnabled(self.section_comboBox))
		self.imageName_checkBox.stateChanged.connect(
			lambda: self.toggleEnabled(self.imageName_lineEdit))
		self.answer1_checkBox.stateChanged.connect(
			lambda: self.toggleEnabled(self.show1_button))
		self.answer2_checkBox.stateChanged.connect(
			lambda: self.toggleEnabled(self.show2_button))
		self.answer3_checkBox.stateChanged.connect(
			lambda: self.toggleEnabled(self.show3_button))
		self.answer4_checkBox.stateChanged.connect(
			lambda: self.toggleEnabled(self.show4_button))

		# Setup the sliders



	def toggleEnabled(self, widget):
		widget.setEnabled(not widget.isEnabled())


	def on_showAnswer(self, tag):

		# Keep track of which answer it is
		self.currentAnswer = tag

		# Desactivate the window
		self.setEnabled(False)

		# Show the dialog to edit the answer
		dialog = QDialog(self)
		answerDialog = AnswerDialog(dialog, self.question_lineEdit.text())
		answerDialog.completed.connect(self.updateAnswers)
		dialog.show()


	def on_send(self):

		# Verify all the fields

		# Send to Firebase

		print('Send')


	def updateAnswers(self, answer):

		# Reactivate window
		self.enabled = True

		print('Updating answer')





