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
	mainWin = None

	def __init__(self, window):

		Ui_MainWindow.__init__(self)
		self.setupUi(window)
		self.setup()
		mainWin = window

	# SETUP

	def setup(self):

		# Setup button connections 
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
		self.academicsMinSlider.setRange(0,100)
		self.academicsMaxSlider.setRange(0,100)
		self.academicsMinSlider.setToolTip(str(self.academicsMaxSlider.value()))
		self.academicsMaxSlider.setToolTip(str(self.academicsMaxSlider.value()))
		self.academicsMinSlider.valueChanged.connect(
			lambda: self.setSliderToolTip(self.academicsMinSlider))
		self.academicsMaxSlider.valueChanged.connect(
			lambda: self.setSliderToolTip(self.academicsMaxSlider))
            
		self.socialMinSlider.setRange(0,100)
		self.socialMaxSlider.setRange(0,100)
		self.socialMinSlider.setToolTip(str(self.socialMinSlider.value()))
		self.socialMaxSlider.setToolTip(str(self.socialMaxSlider.value()))
		self.socialMinSlider.valueChanged.connect(
			lambda: self.setSliderToolTip(self.socialMinSlider))
		self.socialMaxSlider.valueChanged.connect(
			lambda: self.setSliderToolTip(self.socialMaxSlider))
            
		self.financesMinSlider.setRange(0,100)
		self.financesMaxSlider.setRange(0,100)
		self.financesMinSlider.setToolTip(str(self.financesMinSlider.value()))
		self.financesMaxSlider.setToolTip(str(self.financesMaxSlider.value()))
		self.financesMinSlider.valueChanged.connect(
			lambda: self.setSliderToolTip(self.financesMinSlider))
		self.financesMaxSlider.valueChanged.connect(
			lambda: self.setSliderToolTip(self.financesMaxSlider))
            
		self.healthMinSlider.setRange(0,100)
		self.healthMaxSlider.setRange(0,100)
		self.healthMinSlider.setToolTip(str(self.healthMinSlider.value()))
		self.healthMaxSlider.setToolTip(str(self.healthMaxSlider.value()))
		self.healthMinSlider.valueChanged.connect(
			lambda: self.setSliderToolTip(self.healthMinSlider))
		self.healthMaxSlider.valueChanged.connect(
			lambda: self.setSliderToolTip(self.healthMaxSlider))
		
		self.linkSliders(self.academicsMinSlider, self.academicsMaxSlider)
		self.linkSliders(self.socialMinSlider, self.socialMaxSlider)
		self.linkSliders(self.financesMinSlider, self.financesMaxSlider)
		self.linkSliders(self.healthMinSlider, self.healthMaxSlider)

	# HELPERS

	def toggleEnabled(self, widget):
		widget.setEnabled(not widget.isEnabled())


	def setSliderToolTip(self, slider):
		slider.setToolTip(str(slider.value()))


	def updateAnswers(self, answer):
		# Reactivate window
		self.enabled = True

		print('Updating answer')

	def linkSliders(self, minSlider, maxSlider):
		minSlider.valueChanged.connect(
			lambda: maxSlider.setSliderPosition(minSlider.value()) if minSlider.value() >= maxSlider.value() else None)
		maxSlider.valueChanged.connect(
			lambda: minSlider.setSliderPosition(maxSlider.value()) if minSlider.value() >= maxSlider.value() else None)
        

	# ACTIONS

	def on_showAnswer(self, tag):

		# Keep track of which answer it is
		self.currentAnswer = tag

		# Desactivate the window
		self.enabled = False

		# Show the dialog to edit the answer
		dialog = QDialog(parent=self.mainWin)
		answerDialog = AnswerDialog(dialog, self.question_lineEdit.text())
		answerDialog.completed.connect(self.updateAnswers)
		dialog.exec()


	def on_send(self):

		# Verify all the fields

		# Send to Firebase

		print('Send')