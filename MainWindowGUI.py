# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 671))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 29, 491, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.date_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.date_checkBox.setChecked(False)
        self.date_checkBox.setObjectName("date_checkBox")
        self.gridLayout.addWidget(self.date_checkBox, 0, 0, 1, 1)
        self.period_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.period_checkBox.setObjectName("period_checkBox")
        self.gridLayout.addWidget(self.period_checkBox, 1, 0, 1, 1)
        self.period_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.period_comboBox.setObjectName("period_comboBox")
        self.period_comboBox.addItem("")
        self.period_comboBox.addItem("")
        self.gridLayout.addWidget(self.period_comboBox, 1, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 9, 19), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setTime(QtCore.QTime(0, 0, 0))
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(7917, 6, 30), QtCore.QTime(23, 59, 59)))
        self.dateEdit.setMaximumDate(QtCore.QDate(7917, 6, 30))
        self.dateEdit.setMinimumDate(QtCore.QDate(2016, 9, 19))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2016, 9, 19))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 1, 1, 1)
        self.section_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.section_checkBox.setObjectName("section_checkBox")
        self.gridLayout.addWidget(self.section_checkBox, 2, 0, 1, 1)
        self.section_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.section_comboBox.setObjectName("section_comboBox")
        self.section_comboBox.addItem("")
        self.section_comboBox.addItem("")
        self.section_comboBox.addItem("")
        self.gridLayout.addWidget(self.section_comboBox, 2, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(9, 129, 491, 200))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 5, 0, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.financesMaxSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.financesMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.financesMaxSlider.setObjectName("financesMaxSlider")
        self.gridLayout_2.addWidget(self.financesMaxSlider, 3, 3, 1, 1)
        self.financesMinSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.financesMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.financesMinSlider.setObjectName("financesMinSlider")
        self.gridLayout_2.addWidget(self.financesMinSlider, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        self.healthMinSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.healthMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.healthMinSlider.setObjectName("healthMinSlider")
        self.gridLayout_2.addWidget(self.healthMinSlider, 4, 1, 1, 1)
        self.healthMaxSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.healthMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.healthMaxSlider.setObjectName("healthMaxSlider")
        self.gridLayout_2.addWidget(self.healthMaxSlider, 4, 3, 1, 1)
        self.academicsMaxSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.academicsMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.academicsMaxSlider.setObjectName("academicsMaxSlider")
        self.gridLayout_2.addWidget(self.academicsMaxSlider, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.academicsMinSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.academicsMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.academicsMinSlider.setObjectName("academicsMinSlider")
        self.gridLayout_2.addWidget(self.academicsMinSlider, 1, 1, 1, 1)
        self.socialMaxSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.socialMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.socialMaxSlider.setObjectName("socialMaxSlider")
        self.gridLayout_2.addWidget(self.socialMaxSlider, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 3, 1, 1)
        self.socialMinSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.socialMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.socialMinSlider.setObjectName("socialMinSlider")
        self.gridLayout_2.addWidget(self.socialMinSlider, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 7, 0, 1, 1)
        self.acadMin = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acadMin.sizePolicy().hasHeightForWidth())
        self.acadMin.setSizePolicy(sizePolicy)
        self.acadMin.setAlignment(QtCore.Qt.AlignCenter)
        self.acadMin.setObjectName("acadMin")
        self.gridLayout_2.addWidget(self.acadMin, 1, 4, 1, 1)
        self.suiteLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.suiteLabel.setObjectName("suiteLabel")
        self.gridLayout_2.addWidget(self.suiteLabel, 6, 0, 1, 1)
        self.acadMax = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acadMax.sizePolicy().hasHeightForWidth())
        self.acadMax.setSizePolicy(sizePolicy)
        self.acadMax.setAlignment(QtCore.Qt.AlignCenter)
        self.acadMax.setObjectName("acadMax")
        self.gridLayout_2.addWidget(self.acadMax, 1, 5, 1, 1)
        self.tag_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.tag_comboBox.setEditable(True)
        self.tag_comboBox.setObjectName("tag_comboBox")
        self.gridLayout_2.addWidget(self.tag_comboBox, 5, 1, 1, 5)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 6, 1, 1, 5)
        self.socialMin = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.socialMin.sizePolicy().hasHeightForWidth())
        self.socialMin.setSizePolicy(sizePolicy)
        self.socialMin.setAlignment(QtCore.Qt.AlignCenter)
        self.socialMin.setObjectName("socialMin")
        self.gridLayout_2.addWidget(self.socialMin, 2, 4, 1, 1)
        self.finMin = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finMin.sizePolicy().hasHeightForWidth())
        self.finMin.setSizePolicy(sizePolicy)
        self.finMin.setAlignment(QtCore.Qt.AlignCenter)
        self.finMin.setObjectName("finMin")
        self.gridLayout_2.addWidget(self.finMin, 3, 4, 1, 1)
        self.healthMin = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.healthMin.sizePolicy().hasHeightForWidth())
        self.healthMin.setSizePolicy(sizePolicy)
        self.healthMin.setAlignment(QtCore.Qt.AlignCenter)
        self.healthMin.setObjectName("healthMin")
        self.gridLayout_2.addWidget(self.healthMin, 4, 4, 1, 1)
        self.socialMax = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.socialMax.sizePolicy().hasHeightForWidth())
        self.socialMax.setSizePolicy(sizePolicy)
        self.socialMax.setAlignment(QtCore.Qt.AlignCenter)
        self.socialMax.setObjectName("socialMax")
        self.gridLayout_2.addWidget(self.socialMax, 2, 5, 1, 1)
        self.finMax = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finMax.sizePolicy().hasHeightForWidth())
        self.finMax.setSizePolicy(sizePolicy)
        self.finMax.setAlignment(QtCore.Qt.AlignCenter)
        self.finMax.setObjectName("finMax")
        self.gridLayout_2.addWidget(self.finMax, 3, 5, 1, 1)
        self.healthMax = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.healthMax.sizePolicy().hasHeightForWidth())
        self.healthMax.setSizePolicy(sizePolicy)
        self.healthMax.setAlignment(QtCore.Qt.AlignCenter)
        self.healthMax.setObjectName("healthMax")
        self.gridLayout_2.addWidget(self.healthMax, 4, 5, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(9, 29, 491, 193))
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 240, 111, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.send_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy)
        self.send_button.setObjectName("send_button")
        self.verticalLayout_2.addWidget(self.send_button)
        self.statusLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout_2.addWidget(self.statusLabel)
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Critères de sélection de la carte"))
        self.date_checkBox.setText(_translate("MainWindow", "Date"))
        self.period_checkBox.setText(_translate("MainWindow", "Période"))
        self.period_comboBox.setItemText(0, _translate("MainWindow", "Semaine"))
        self.period_comboBox.setItemText(1, _translate("MainWindow", "Week-end"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.section_checkBox.setText(_translate("MainWindow", "Section"))
        self.section_comboBox.setItemText(0, _translate("MainWindow", "Meca"))
        self.section_comboBox.setItemText(1, _translate("MainWindow", "IC"))
        self.section_comboBox.setItemText(2, _translate("MainWindow", "GC"))
        self.label_4.setText(_translate("MainWindow", "Finances"))
        self.label.setText(_translate("MainWindow", "Académique"))
        self.label_3.setText(_translate("MainWindow", "Social"))
        self.label_7.setText(_translate("MainWindow", "Min"))
        self.label_6.setText(_translate("MainWindow", "Range de sélection"))
        self.label_5.setText(_translate("MainWindow", "Santé"))
        self.label_8.setText(_translate("MainWindow", "Max"))
        self.label_9.setText(_translate("MainWindow", "Tag"))
        self.acadMin.setText(_translate("MainWindow", "0"))
        self.suiteLabel.setText(_translate("MainWindow", "Suite"))
        self.acadMax.setText(_translate("MainWindow", "0"))
        self.socialMin.setText(_translate("MainWindow", "0"))
        self.finMin.setText(_translate("MainWindow", "0"))
        self.healthMin.setText(_translate("MainWindow", "0"))
        self.socialMax.setText(_translate("MainWindow", "0"))
        self.finMax.setText(_translate("MainWindow", "0"))
        self.healthMax.setText(_translate("MainWindow", "0"))
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
        self.statusLabel.setText(_translate("MainWindow", "status"))

