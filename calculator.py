# -*- python 3.8.10 -*-
# -*- coding:utf-8 -*-
####################################################################################################
# File: \main.py                                                                                   #
# Project: Calculator                                                                              #
# Created Date: Thursday Oct 28th 2021, 9:18:31 pm                                                 #
# Author: Wenren Muyan                                                                             #
# Comments:                                                                                        #
# --------------------------------------------------------------------------------                 #
# Last Modified: 2/11/2021 07:39:43                                                                #
# Modified By: Wenren Muyan                                                                        #
# --------------------------------------------------------------------------------                 #
# Copyright (c) 2021 - future Wenren Muyan                                                         #
# --------------------------------------------------------------------------------                 #
# HISTORY:                                                                                         #
# Date				By				Comments                                                       #
# --------------------------------------------------------------------------------                 #
####################################################################################################

import sys

from PySide2.QtWidgets import QApplication
from PySide2 import QtCore
from gui import mainWindow
from core import coreCalc


class mainProg():
    def __init__(self):
        self.window = mainWindow.calcGUI()
        self.calc = coreCalc.calcCore()
        self.widgetFunction()

    def windowShow(self):
        self.window.show()

    def widgetFunction(self):
        self.window.buttonDiff.clicked.connect(self.Diff)
        self.window.buttonInteg.clicked.connect(self.Integ)
        self.window.buttonLimit.clicked.connect(self.Limit)
        self.window.docsAct.triggered.connect(self.Docs)

    @QtCore.Slot()
    def Diff(self):
        ### for test ###
        self.edit = [self.window.editDiffInput.text(), self.window.editDiffSymbols.text(),
                     self.window.editDiffSeq.text(), ""]
        ### for test ###
        self.calc.calcDispatcher(self.edit, "Derivate")
        self.window.setCanvas()
        self.window.resLatexCanvas.dispalyRes(self.calc.output)
        self.window.resLatexCanvas.draw()

    @QtCore.Slot()
    def Integ(self):
        ### for test ###
        self.edit = [self.window.editIntegInput.text(), self.window.editIntegSymbols.text(),
                     self.window.editIntegRange.text(), ""]
        ### for test ###
        self.calc.calcDispatcher(self.edit, "Integrate")
        self.window.setCanvas()
        self.window.resLatexCanvas.dispalyRes(self.calc.output)
        self.window.resLatexCanvas.draw()

    @QtCore.Slot()
    def Limit(self):
        self.edit = [self.window.editLimitInput.text(), self.window.editLimitSymbols.text(),
                     self.window.editLimitVal.text(), ""]
        ### for test ###
        self.calc.calcDispatcher(self.edit, "Limit")
        self.window.setCanvas()
        self.window.resLatexCanvas.dispalyRes(self.calc.output)
        self.window.resLatexCanvas.draw()

    @QtCore.Slot()
    def Docs(self):
        self.window.showDocs()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    prog = mainProg()
    prog.windowShow()

    sys.exit(app.exec_())
