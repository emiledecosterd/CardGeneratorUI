import sys

# Qt classes
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Custom classes
from MainWindow import MainWindow



if __name__ == '__main__':

	# Create application
	app = QApplication(sys.argv)

	# Initialize main window
	window = QMainWindow()
	controller = MainWindow(window)
	window.show()
	
	sys.exit(app.exec_())