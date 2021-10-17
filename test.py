# -*- python 3.8.10 -*-
# -*- coding:utf-8 -*-
####################################################################################################
  # File: \test.py                                                                                 #
  # Project: Calculator                                                                            #
  # Created Date: Saturday Oct 16th 2021, 9:20:19 pm                                               #
  # Author: Wenren Muyan                                                                           #
  # Comments:                                                                                      #
  # --------------------------------------------------------------------------------               #
  # Last Modified: 0/10/2021 08:55:22                                                              #
  # Modified By: Wenren Muyan                                                                      #
  # --------------------------------------------------------------------------------               #
  # Copyright (c) 2021 - future Wenren Muyan                                                       #
  # --------------------------------------------------------------------------------               #
  # HISTORY:                                                                                       #
  # Date				By				Comments                                                   #
  # --------------------------------------------------------------------------------               #
####################################################################################################


import sys

from PySide6.QtWidgets import (QApplication, QVBoxLayout, QWidget, QPushButton, QGridLayout, QLabel)
from PySide6 import QtCore

class Form(QWidget):
	def __init__(self):
		super(Form,self).__init__()

		self.layout = QVBoxLayout()
		
		self.button_1 = QPushButton("button_1")
		self.button_2 = QPushButton("button_2")
		self.button_3 = QPushButton("button_3")
		self.button_3.setObjectName("button_3")

		self.layout.addWidget(self.button_1)
		self.layout.addWidget(self.button_2)
		self.layout.addWidget(self.button_3)

		self.setLayout(self.layout)

		'''
		with open("./style/button.qss", "r") as f:
			_style = f.read()
			self.setStyleSheet(_style)
		'''


if __name__ == "__main__":
	app = QApplication([])

	myForm = Form()
	myForm.show()

	with open("./style/button.qss", "r") as f:
		_style = f.read()
		myForm.setStyleSheet(_style)

	sys.exit(app.exec())

	