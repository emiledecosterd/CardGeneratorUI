import sys
import pyrebase
import json

# Qt classes
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Custom classes
from MainWindowGUI import Ui_MainWindow
from Answer import Answer
from AnswerDialog import AnswerDialog
from Card import Card

'''
/!\
	MAKE GUI CLASS QWIDGET SUBCLASS!!! 
	QtWidgets.QWidget
	(otherwise signals won't work)
/!\
'''

class MainWindow(Ui_MainWindow):

	currentAnswer = None
	answers = [None, None, None, None]
	mainWin = None
	fb = None
	startDate = QDate(2016, 9, 20)

	def __init__(self, window):

		Ui_MainWindow.__init__(self)
		self.setupUi(window)
		self.setup()
		mainWin = window
		config = {
		  "apiKey": "AIzaSyBUqtGx5JnZnLVclM-kRVhi-06jb1uBnOE",
		  "authDomain": "epflsurvival-abd33.firebaseapp.com",
		  "storageBucket": "epflsurvival-abd33.appspot.com",
		  "databaseURL": "https://epflsurvival-abd33.firebaseio.com/"
		}

		self.fb = pyrebase.initialize_app(config)
	# SETUP

	def setup(self):

		# Setup button connections 
		self.send_button.clicked.connect(self.on_send)
		self.show1_button.clicked.connect(lambda: self.on_showAnswer(0))
		self.show2_button.clicked.connect(lambda: self.on_showAnswer(1))
		self.show3_button.clicked.connect(lambda: self.on_showAnswer(2))
		self.show4_button.clicked.connect(lambda: self.on_showAnswer(3))

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
		self.answers[self.currentAnswer] = answer
		print("Update done")

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
		answerDialog = AnswerDialog(dialog, self.question_lineEdit.text(), self.answers[tag])
		answerDialog.completed.connect(self.updateAnswers)
		dialog.exec()


	def on_send(self):
	
		messageBox = QMessageBox()
		errors = ""
		
		# Verify all the fields
		if self.question_lineEdit.text() == "":
			errors += '-> Il doit y avoir une question!' + '\n'
			
		c = 0
		for a in self.answers:
			if a == None:
				c += 1
				
		if c > 2:
			errors += '-> Il faut au moins 2 réponses!' + '\n'
			
		if errors != "":
			messageBox.setText(errors)
			messageBox.exec()
			return
			
		date = -1
		if self.date_checkBox.isChecked():
			date = self.startDate.daysTo(self.dateEdit.date())
			
		period = -1
		if self.period_checkBox.isChecked():
			period = self.period_comboBox.currentIndex()
			
		section = -1
		if self.section_checkBox.isChecked():
			section = self.section_comboBox.currentIndex()
			
		ranges = {
			"academics" : [self.academicsMinSlider.value(), self.academicsMaxSlider.value()],
			"social" : [self.socialMinSlider.value(), self.socialMaxSlider.value()],
			"finances" : [self.financesMinSlider.value(), self.financesMaxSlider.value()],
			"health" : [self.healthMinSlider.value(), self.healthMaxSlider.value()]
		}
		
		image = ""
		if self.imageName_checkBox.isChecked():
			image = self.imageName_lineEdit.text()
			
		tag = ""
		if self.tag_comboBox.currentText() != "":
			tag = self.tag_comboBox.currentText()
			
		suite = ""
		if self.comboBox.currentIndex() > 0:
			suite = self.comboBox.currentText()
			
		# Send to Firebase
		card = Card(self.question_lineEdit.text(), 
					self.answers,
					ranges,
					date,
					period,
					section,
					image,
					tag,
					suite)
					
		#print(json.dumps(self.answers, default=lambda o: o.__dict__))
		#print(card.toJSON())
		auth = self.fb.auth()

		# Log the user in
		user = auth.sign_in_with_email_and_password('gui@survival.ch', 'Shd&5sdA_9(al')

		db = self.fb.database()
		r = db.child('cards').push(json.loads(card.toJSON()), user['idToken'])
		print(r)
		print('Send')