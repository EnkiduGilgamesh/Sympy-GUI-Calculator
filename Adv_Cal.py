# -*- python 3.8.10 -*-
# -*- coding:utf-8 -*-
####################################################################################################
  # File: \Adv_Cal.py                                                                              #
  # Project: Calculator                                                                            #
  # Created Date: Wednesday Oct 13th 2021, 8:52:43 am                                              #
  # Author: Wenren Muyan                                                                           #
  # Comments:                                                                                      #
  # --------------------------------------------------------------------------------               #
  # Last Modified: 0/10/2021 08:57:6                                                               #
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

class Advanced_Calculator(QWidget):
	def __init__(self):
		super(Advanced_Calculator,self).__init__()

		self.layout = QVBoxLayout()

		self.layout.addWidget(self.init_operator_button())
		self.layout.addWidget(self.init_number_button())

		self.setLayout(self.layout)


	def init_operator_button(self):
		layout_operator = QGridLayout()
		operator_widget = QWidget()

		button_plus = QPushButton("+")
		button_minu = QPushButton("-")
		button_prod = QPushButton("x")
		button_divi = QPushButton("/")

		button_plus.setObjectName("button_plus")

		layout_operator.addWidget(button_plus,0,0,1,1) # alignment=QtCore.Qt.AlignCenter
		layout_operator.addWidget(button_minu,0,1,1,1)
		layout_operator.addWidget(button_prod,0,2,1,1)
		layout_operator.addWidget(button_divi,0,3,1,1)

		operator_widget.setLayout(layout_operator)

		return operator_widget

	def init_number_button(self):
		layout_number = QGridLayout()
		number_widget = QWidget()

		button_number_0 = QPushButton("0")
		button_number_1 = QPushButton("1")
		button_number_2 = QPushButton("2")
		button_number_3 = QPushButton("3")
		button_number_4 = QPushButton("4")
		button_number_5 = QPushButton("5")
		button_number_6 = QPushButton("6")
		button_number_7 = QPushButton("7")
		button_number_8 = QPushButton("8")
		button_number_9 = QPushButton("9")

		# button_dot = QPushButton(".")
		# button_back = QPushButton("Backspace")

		layout_number.addWidget(button_number_1,0,0,1,1)
		layout_number.addWidget(button_number_2,0,1,1,1)
		layout_number.addWidget(button_number_3,0,2,1,1)
		layout_number.addWidget(button_number_4,1,0,1,1)
		layout_number.addWidget(button_number_5,1,1,1,1)
		layout_number.addWidget(button_number_6,1,2,1,1)
		layout_number.addWidget(button_number_7,2,0,1,1)
		layout_number.addWidget(button_number_8,2,1,1,1)
		layout_number.addWidget(button_number_9,2,2,1,1)
		layout_number.addWidget(button_number_0,3,0,1,3)

		number_widget.setLayout(layout_number)

		return number_widget



if __name__ == "__main__":
	app = QApplication([])

	Calculator = Advanced_Calculator()
	# Calculator.resize(800, 600)
	Calculator.show()

	with open("./style/button.qss", "r") as f:
		_style = f.read()
		Calculator.setStyleSheet(_style)

	sys.exit(app.exec())
