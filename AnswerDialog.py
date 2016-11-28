# Qt classes
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Custom classes
from AnswersDialogGUI import Ui_Dialog
from Answer import Answer

'''
/!\
	MAKE GUI CLASS QWIDGET SUBCLASS!!! 
	QtWidgets.QWidget
	(otherwise signals won't work)
/!\
'''

class AnswerDialog(Ui_Dialog):

	completed = pyqtSignal(Answer)
	dialogRef = None

	def __init__(self, dialog, question, answer):

		# Setup user interface
		Ui_Dialog.__init__(self)
		self.setupUi(dialog)
		self.setupSliders()
		self.questionLabel.setText(question)
		
		if answer != None:
			print(answer.comment)
			self.comment_lineEdit.setText(answer.comment)
			self.answerText_lineEdit.setText(answer.answer)
			self.academicsSlider.setValue(answer.changes['academics'])
			self.socialSlider.setValue(answer.changes['social'])
			self.financesSlider.setValue(answer.changes['finances'])
			self.healthSlider.setValue(answer.changes['health'])
		
		# Setup connections
		self.buttonBox.accepted.connect(self.on_validate)

		self.resetButton.clicked.connect(self.resetSliders)
		
		self.academicsSlider.valueChanged.connect(lambda:
			self.labelSliderAca.setText(str(self.academicsSlider.value())))
		self.socialSlider.valueChanged.connect(lambda:
			self.labelSliderSoc.setText(str(self.socialSlider.value())))
		self.financesSlider.valueChanged.connect(lambda:
			self.labelSliderFin.setText(str(self.financesSlider.value())))
		self.healthSlider.valueChanged.connect(lambda:
			self.labelSliderHea.setText(str(self.healthSlider.value())))
		
		self.dialogRef = dialog


	def resetSliders(self):
			self.academicsSlider.setValue(0)
			self.socialSlider.setValue(0)
			self.financesSlider.setValue(0)
			self.healthSlider.setValue(0)
	
	# Define min and max value for each gauge
	def setupSliders(self):
		max = 100
		min = -max
		
		self.academicsSlider.setRange(min, max)
		self.academicsSlider.setValue(0)
		self.socialSlider.setRange(min, max)
		self.socialSlider.setValue(0)
		self.financesSlider.setRange(min, max)
		self.financesSlider.setValue(0)
		self.healthSlider.setRange(min, max)
		self.healthSlider.setValue(0)


	# The user pressed "ok", validate what he/she did
	def on_validate(self):

		# Get the user input
		answerText = self.answerText_lineEdit.text()
		commentText = self.comment_lineEdit.text()

		# Verify it 
		if answerText is not None and answerText is not "":

			if commentText == "":
				commentText = None

			changes = {
				'academics' : self.academicsSlider.value(),
				'social' : self.socialSlider.value(),
				'finances' : self.financesSlider.value(),
				'health' : self.healthSlider.value()
			}

			# Everything is ok, emit completed signal and dismiss the dialog
			answer = Answer(answerText, changes, commentText)
			self.completed.emit(answer)
			self.dialogRef.accept()

		else:
			messageBox = QMessageBox()
			messageBox.setText('La réponse ne doit pas être vide!')
			messageBox.exec()

