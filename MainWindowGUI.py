# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 29, 341, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.date_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.date_checkBox.setObjectName("date_checkBox")
        self.gridLayout.addWidget(self.date_checkBox, 0, 0, 1, 1)
        self.period_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.period_checkBox.setObjectName("period_checkBox")
        self.gridLayout.addWidget(self.period_checkBox, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 1, 1, 1)
        self.section_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.section_checkBox.setObjectName("section_checkBox")
        self.gridLayout.addWidget(self.section_checkBox, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 129, 341, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.academicsMaxSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.academicsMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.academicsMaxSlider.setObjectName("academicsMaxSlider")
        self.gridLayout_2.addWidget(self.academicsMaxSlider, 1, 2, 1, 1)
        self.academicsMinSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.academicsMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.academicsMinSlider.setObjectName("academicsMinSlider")
        self.gridLayout_2.addWidget(self.academicsMinSlider, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.socialMinSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.socialMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.socialMinSlider.setObjectName("socialMinSlider")
        self.gridLayout_2.addWidget(self.socialMinSlider, 2, 1, 1, 1)
        self.socialMaxSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.socialMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.socialMaxSlider.setObjectName("socialMaxSlider")
        self.gridLayout_2.addWidget(self.socialMaxSlider, 2, 2, 1, 1)
        self.financesMinSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.financesMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.financesMinSlider.setObjectName("financesMinSlider")
        self.gridLayout_2.addWidget(self.financesMinSlider, 3, 1, 1, 1)
        self.financesMaxSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.financesMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.financesMaxSlider.setObjectName("financesMaxSlider")
        self.gridLayout_2.addWidget(self.financesMaxSlider, 3, 2, 1, 1)
        self.healthMinSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.healthMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.healthMinSlider.setObjectName("healthMinSlider")
        self.gridLayout_2.addWidget(self.healthMinSlider, 4, 1, 1, 1)
        self.healthMaxSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.healthMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.healthMaxSlider.setObjectName("healthMaxSlider")
        self.gridLayout_2.addWidget(self.healthMaxSlider, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)
        self.gridLayoutWidget.raise_()
        self.gridLayoutWidget_2.raise_()
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(9, 29, 341, 193))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.answer2_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.answer2_checkBox.setObjectName("answer2_checkBox")
        self.gridLayout_3.addWidget(self.answer2_checkBox, 3, 0, 1, 1)
        self.imageName_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.imageName_checkBox.setObjectName("imageName_checkBox")
        self.gridLayout_3.addWidget(self.imageName_checkBox, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.imageName_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.imageName_lineEdit.setObjectName("imageName_lineEdit")
        self.gridLayout_3.addWidget(self.imageName_lineEdit, 0, 1, 1, 1)
        self.question_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.question_lineEdit.setObjectName("question_lineEdit")
        self.gridLayout_3.addWidget(self.question_lineEdit, 1, 1, 1, 1)
        self.answer3_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.answer3_checkBox.setObjectName("answer3_checkBox")
        self.gridLayout_3.addWidget(self.answer3_checkBox, 4, 0, 1, 1)
        self.answer1_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.answer1_checkBox.setObjectName("answer1_checkBox")
        self.gridLayout_3.addWidget(self.answer1_checkBox, 2, 0, 1, 1)
        self.answer4_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.answer4_checkBox.setObjectName("answer4_checkBox")
        self.gridLayout_3.addWidget(self.answer4_checkBox, 5, 0, 1, 1)
        self.show1_button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.show1_button.setObjectName("show1_button")
        self.gridLayout_3.addWidget(self.show1_button, 2, 1, 1, 1)
        self.show2_button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.show2_button.setObjectName("show2_button")
        self.gridLayout_3.addWidget(self.show2_button, 3, 1, 1, 1)
        self.show3_button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.show3_button.setObjectName("show3_button")
        self.gridLayout_3.addWidget(self.show3_button, 4, 1, 1, 1)
        self.show4_button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.show4_button.setObjectName("show4_button")
        self.gridLayout_3.addWidget(self.show4_button, 5, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.send_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.send_button.setObjectName("send_button")
        self.verticalLayout.addWidget(self.send_button)
        self.verticalLayout.setStretch(0, 60)
        self.verticalLayout.setStretch(1, 45)
        self.verticalLayout.setStretch(2, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Critères de sélection de la carte"))
        self.date_checkBox.setText(_translate("MainWindow", "Date"))
        self.period_checkBox.setText(_translate("MainWindow", "Période"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Semaine"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Week-end"))
        self.section_checkBox.setText(_translate("MainWindow", "Section"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Meca"))
        self.comboBox.setItemText(1, _translate("MainWindow", "IC"))
        self.comboBox.setItemText(2, _translate("MainWindow", "GC"))
        self.label.setText(_translate("MainWindow", "Académique"))
        self.label_3.setText(_translate("MainWindow", "Social"))
        self.label_4.setText(_translate("MainWindow", "Finances"))
        self.label_5.setText(_translate("MainWindow", "Santé"))
        self.label_6.setText(_translate("MainWindow", "Range de sélection"))
        self.label_7.setText(_translate("MainWindow", "Min"))
        self.label_8.setText(_translate("MainWindow", "Max"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Contenu de la carte"))
        self.answer2_checkBox.setText(_translate("MainWindow", "Réponse 2"))
        self.imageName_checkBox.setText(_translate("MainWindow", "Image"))
        self.label_2.setText(_translate("MainWindow", "Question"))
        self.imageName_lineEdit.setPlaceholderText(_translate("MainWindow", "Entrer le nom de l\'image"))
        self.question_lineEdit.setPlaceholderText(_translate("MainWindow", "Posez votre question"))
        self.answer3_checkBox.setText(_translate("MainWindow", "Réponse 3"))
        self.answer1_checkBox.setText(_translate("MainWindow", "Réponse 1"))
        self.answer4_checkBox.setText(_translate("MainWindow", "Réponse 4"))
        self.show1_button.setText(_translate("MainWindow", "Afficher"))
        self.show2_button.setText(_translate("MainWindow", "Afficher"))
        self.show3_button.setText(_translate("MainWindow", "Afficher"))
        self.show4_button.setText(_translate("MainWindow", "Afficher"))
        self.send_button.setText(_translate("MainWindow", "Envoyer!"))

