import sys

# Qt classes
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Custom classes
from Answer import Answer


class AnswerDialog(Ui_Dialog):

	completed = pyqtSignal(Answer)

	def __init__(self, dialog, question):

		# Setup user interface
		Ui_Dialog.__init__(self)
		self.setupUi(dialog)
		self.setupSliders()
		self.questionLabel.setText(question)

		# Setup connections
		self.buttonBox.accepted.connect(self.on_validate)


	# Define min and max value for each gauge
	def setupSliders(self):

		self.academicsSlider.setRange(-15,15)
		self.academicsSlider.setValue(0)
		self.socialSlider.setRange(-15,15)
		self.socialSlider.setValue(0)
		self.financesSlider.setRange(-15,15)
		self.financesSlider.setValue(0)
		self.healthSlider.setRange(-15,15)
		self.healthSlider.setValue(0)


	# The user pressed "ok", validate what he/she did
	def on_validate(self):

		# Get the user input
		answerText = self.answerText_lineEdit.text
		commentText = self.comment_lineEdit.text

		# Verify it 
		if answerText is not None and answerText is not "":

			if commentText == "":
				commentText = None

			changes = {
				'academics' : self.academicsSlider.value,
				'social' : self.socialSlider.value,
				'finances' : self.financesSlider.value,
				'health' : self.healthSlider.value
			}

			# Everything is ok, emit completed signal and dismiss the dialog
			answer = Answer(answerText, changes, commentText)
			self.completed.emit(answer)
			self.accept()

		else:
			messageBox = QMessageBox('La réponse ne doit pas être vide!')
			messageBox.show()

