# -*- python 3.8.10 -*-
# -*- coding:utf-8 -*-
####################################################################################################
# File: \differential.py                                                                           #
# Project: Calculator                                                                              #
# Created Date: Monday Oct 25th 2021, 7:29:31 pm                                                   #
# Author: Wenren Muyan                                                                             #
# Comments:                                                                                        #
# --------------------------------------------------------------------------------                 #
# Last Modified: 26/10/2021 10:09:51                                                               #
# Modified By: Wenren Muyan                                                                        #
# --------------------------------------------------------------------------------                 #
# Copyright (c) 2021 - future Wenren Muyan                                                         #
# --------------------------------------------------------------------------------                 #
# HISTORY:                                                                                         #
# Date				By				Comments                                                       #
# --------------------------------------------------------------------------------                 #
####################################################################################################

import sys
import re as reS

from sympy import *
from PySide6.QtWidgets import (QApplication, QPushButton, QTextBrowser, QVBoxLayout, \
                               QWidget, QGridLayout, QTextEdit, QLabel, QLineEdit)
from PySide6 import QtCore


class differential(QWidget):
    def __init__(self, parent=None):
        super(differential, self).__init__(parent)

        self.initMainWindow()
        self.layoutManagement()

        self.setLayout(self.main_window)

    def initMainWindow(self):
        # text
        self.text_input = ""
        self.text_output = ""
        self.text_symbols = ""
        self.text_diff_symbols = ""

        # line edit

        self.edit_output = QTextEdit(self.text_output)
        self.edit_input = QLineEdit()

        self.edit_output.setPlaceholderText("output")
        self.edit_input.setPlaceholderText("input")

        # symbols
        self.edit_symbols = QLineEdit()
        self.edit_diff_symbols = QLineEdit()
        self.label_symbols = QLabel("Symbols: ")
        self.label_diff_symbols = QLabel("Diff Symbols: ")

        self.edit_symbols.setPlaceholderText("Symbols that the function will use")
        self.edit_diff_symbols.setPlaceholderText("Sequence that differentiate the function")

        # button
        self.button_diff = QPushButton("Differentiate")
        self.button_diff.clicked.connect(self.cal_diff)

    def layoutManagement(self):
        self.main_window = QVBoxLayout()

        self.widget_symbols = QWidget()
        self.layout_symbols = QGridLayout()

        self.layout_symbols.addWidget(self.edit_symbols, 1, 0, 1, 4)
        self.layout_symbols.addWidget(self.edit_diff_symbols, 1, 4, 1, 4)
        self.layout_symbols.addWidget(self.label_symbols, 0, 0, 1, 4)
        self.layout_symbols.addWidget(self.label_diff_symbols, 0, 4, 1, 4)

        self.layout_symbols.setAlignment(self.edit_symbols, QtCore.Qt.AlignLeft)
        self.layout_symbols.setAlignment(self.edit_diff_symbols, QtCore.Qt.AlignLeft)
        self.layout_symbols.setAlignment(self.label_symbols, QtCore.Qt.AlignLeft)
        self.layout_symbols.setAlignment(self.label_diff_symbols, QtCore.Qt.AlignLeft)

        self.widget_symbols.setLayout(self.layout_symbols)

        self.main_window.addWidget(self.edit_input)
        self.main_window.addWidget(self.widget_symbols)
        self.main_window.addWidget(self.edit_output)
        self.main_window.addWidget(self.button_diff)

    @QtCore.Slot()
    def cal_diff(self):
        oper_symbols = ""
        # print()
        oper_symbols = reS.split(" +", self.edit_symbols.text())

        for i in range(0, len(oper_symbols)):
            exec("{} = symbols('{}')".format(oper_symbols[i], oper_symbols[i]))

        diff_sequence_symbols = ""
        diff_sequence_symbols = reS.split(" +", self.edit_diff_symbols.text())

        diff_cmd = ""

        for i in range(0, len(diff_sequence_symbols)):
            diff_cmd += ","
            diff_cmd += diff_sequence_symbols[i]

        # print(diff_cmd)
        # print("sympy.diff({}{})".format(self.edit_input.text(), diff_cmd))
        self.text_output = str(eval("latex(diff({}{}))".format(self.edit_input.text(), diff_cmd)))

        self.edit_output.toMarkdown()
        self.edit_output.setMarkdown("${}$".format(self.text_output))

        #self.edit_output.setText("##\n")
        #self.edit_output.setText("{}\n".format(self.text_output))
        #self.edit_output.setText("##")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    di = differential()
    di.show()

    sys.exit(app.exec())
