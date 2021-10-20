# -*- python 3.8.10 -*-
# -*- coding:utf-8 -*-
####################################################################################################
# File: \Adv_Cal.py                                                                                #
# Project: Calculator                                                                              #
# Created Date: Wednesday Oct 13th 2021, 8:52:43 am                                                #
# Author: Wenren Muyan                                                                             #
# Comments:                                                                                        #
# --------------------------------------------------------------------------------                 #
# Last Modified: 20/10/2021 10:41:45                                                               #
# Modified By: Wenren Muyan                                                                        #
# --------------------------------------------------------------------------------                 #
# Copyright (c) 2021 - future Wenren Muyan                                                         #
# --------------------------------------------------------------------------------                 #
# HISTORY:                                                                                         #
# Date				By				Comments                                                       #
# --------------------------------------------------------------------------------                 #
####################################################################################################


import sys

from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget, QToolButton, QGridLayout, QLineEdit)
from PySide6 import QtCore


class Advanced_Calculator(QWidget):
    def __init__(self):
        super(Advanced_Calculator, self).__init__()

        self.init_interface()

        self.init_widget_functions()

        self.none_input = 1
        self.none_output = 1

    def init_interface(self):
        self.mainwindow = QGridLayout(self)

        # Digit buttons and operator buttons

        self.widget_button = QWidget()

        self.button_digit = []

        for i in range(0, 10):
            self.button_digit.append(Button(str(i)))

        self.button_factor = Button("!")
        self.button_lbracket = Button("(")
        self.button_rbracket = Button(")")
        self.button_backspace = Button("<-")
        self.button_division = Button("/")
        self.button_log = Button("log")
        self.button_multiply = Button("*")
        self.button_sqrt = Button("√")
        self.button_minus = Button("-")
        self.button_power = Button("^")
        self.button_plus = Button("+")
        self.button_abs = Button("|x|")
        self.button_const = Button("Const")
        self.button_dot = Button(".")
        self.button_equal = Button("=")

        # Text input and output

        self.widget_display = QWidget()

        self.display_input = QLineEdit()
        self.display_output = QLineEdit()

        self.display_input.setReadOnly(True)
        self.display_input.setAlignment(QtCore.Qt.AlignRight)

        self.display_output.setReadOnly(True)
        self.display_output.setAlignment(QtCore.Qt.AlignRight)

        # Buttons layout with 0 spacing

        self.layout_button = QGridLayout()
        self.layout_button.setSpacing(0)

        self.layout_button.addWidget(self.button_factor, 0, 0, 1, 1)
        self.layout_button.addWidget(self.button_lbracket, 0, 1, 1, 1)
        self.layout_button.addWidget(self.button_rbracket, 0, 2, 1, 1)
        self.layout_button.addWidget(self.button_backspace, 0, 3, 1, 1)
        self.layout_button.addWidget(self.button_division, 0, 4, 1, 1)
        self.layout_button.addWidget(self.button_log, 1, 0, 1, 1)

        for i in range(1, 10):
            self.layout_button.addWidget(self.button_digit[i], 3 - ((i - 1) // 3), (i - 1) % 3 + 1, 1, 1)

        self.layout_button.addWidget(self.button_multiply, 1, 4, 1, 1)
        self.layout_button.addWidget(self.button_sqrt, 2, 0, 1, 1)
        self.layout_button.addWidget(self.button_minus, 2, 4, 1, 1)
        self.layout_button.addWidget(self.button_power, 3, 0, 1, 1)
        self.layout_button.addWidget(self.button_plus, 3, 4, 1, 1)
        self.layout_button.addWidget(self.button_power, 3, 0, 1, 1)
        self.layout_button.addWidget(self.button_power, 3, 0, 1, 1)
        self.layout_button.addWidget(self.button_power, 3, 0, 1, 1)
        self.layout_button.addWidget(self.button_power, 3, 0, 1, 1)
        self.layout_button.addWidget(self.button_abs, 4, 0, 1, 1)
        self.layout_button.addWidget(self.button_const, 4, 1, 1, 1)
        self.layout_button.addWidget(self.button_digit[0], 4, 2, 1, 1)
        self.layout_button.addWidget(self.button_dot, 4, 3, 1, 1)
        self.layout_button.addWidget(self.button_equal, 4, 4, 1, 1)

        self.widget_button.setLayout(self.layout_button)

        # Display widget layout

        self.layout_display = QGridLayout()

        self.layout_display.addWidget(self.display_output, 0, 0, 2, 5)
        self.layout_display.addWidget(self.display_input, 3, 0, 2, 5)

        self.widget_display.setLayout(self.layout_display)

        # layouts set to mainwindow

        self.mainwindow.addWidget(self.widget_display, 0, 0, 6, 5)
        self.mainwindow.addWidget(self.widget_button, 8, 0, 6, 5)

    def init_widget_functions(self):
        # display lines
        self.text_input = ("Input")
        self.text_output = ("Output")

        self.display_input.setText(self.text_input)
        self.display_output.setText(self.text_output)

        # buttons connect functions

        for i in range(0, 10):
            self.button_digit[i].clicked.connect(self.get_oper)

        self.button_lbracket.clicked.connect(self.get_oper)
        self.button_rbracket.clicked.connect(self.get_oper)
        self.button_division.clicked.connect(self.get_oper)
        self.button_multiply.clicked.connect(self.get_oper)
        self.button_minus.clicked.connect(self.get_oper)
        self.button_plus.clicked.connect(self.get_oper)
        self.button_dot.clicked.connect(self.get_oper)

        # special functions button

        self.button_power.clicked.connect(self.get_power_oper)

        self.button_backspace.clicked.connect(self.backspace)

        self.button_equal.clicked.connect(self.calculate_res)

    @QtCore.Slot()
    def get_oper(self):
        clicked_button = QtCore.QObject.sender(self)

        if self.none_input == 1:
            self.text_input = ""
            self.none_input = 0

        self.text_input += clicked_button.text()

        self.display_input.setText(self.text_input)

    @QtCore.Slot()
    def calculate_res(self):
        if self.none_output == 1:
            self.text_output = ""
            self.none_output = 0

        self.text_output = str(eval(self.text_input))

        self.display_output.setText(self.text_output)

    @QtCore.Slot()
    def get_power_oper(self):
        if self.none_input == 1:
            return
        else:
            self.text_input += "**"

        self.display_input.setText(self.text_input)

    @QtCore.Slot()
    def backspace(self):
        if self.none_input != 1 and len(self.text_input) != 1:
            self.text_input = self.text_input[:(len(self.text_input)-1)]

            self.display_input.setText(self.text_input)

        elif self.none_input != 1 and len(self.text_input) == 1:
            self.text_input = ("Input")
            self.none_input = 1

            self.display_input.setText(self.text_input)

        else:
            pass


class Button(QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self) -> QtCore.QSize:
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))

        # size.rheight() += 20
        # size.rwidth() = max(size.width(), size.height())

        return size


if __name__ == "__main__":
    app = QApplication([])

    Calculator = Advanced_Calculator()
    Calculator.show()

    '''
    with open("./style/button.qss", "r") as f:
        _style = f.read()
        Calculator.setStyleSheet(_style)
    '''

    sys.exit(app.exec())
