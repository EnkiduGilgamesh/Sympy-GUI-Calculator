# -*- python 3.8.10 -*-
# -*- coding:utf-8 -*-
####################################################################################################
# File: \mainWindow.py                                                                             #
# Project: gui                                                                                     #
# Created Date: Thursday Oct 28th 2021, 7:56:51 pm                                                 #
# Author: Wenren Muyan                                                                             #
# Comments: Make a user interface                                                                  #
# --------------------------------------------------------------------------------                 #
# Last Modified: 2/11/2021 08:56:12                                                                #
# Modified By: Wenren Muyan                                                                        #
# --------------------------------------------------------------------------------                 #
# Copyright (c) 2021 - future Wenren Muyan                                                         #
# --------------------------------------------------------------------------------                 #
# HISTORY:                                                                                         #
# Date				By				Comments                                                       #	
# 
# 2021-11-2		    WR-MY			complete docs
# 
# 2021-11-2		    WR-MY			complete calc tab widgets
# 
# 2021-10-28		WR-MY			complete top menu
# --------------------------------------------------------------------------------                 #
####################################################################################################


from PySide2.QtWidgets import (QPushButton, QGridLayout,
                               QWidget, QLabel, QLineEdit, QGraphicsScene,
                               QGraphicsView, QMenu, QMenuBar, QAction,
                               QTabWidget, QVBoxLayout)
from PySide2 import QtCore
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtGui import QIcon

from . import pltView


class calcGUI(QWidget):
    def __init__(self, parent=None):
        super(calcGUI, self).__init__(parent)
        
        self.setWindow()

        self.initMenu()
        self.initTabBar()
        self.initView()
        self.setCanvas()
        self.layoutMgnt()

        self.initDocs()

    def sizeHint(self) -> QtCore.QSize:
        size = super(calcGUI, self).sizeHint()
        # size.setWidth(size.width() + 400)
        # size.setHeight(size.height())
        return size

    def setWindow(self):
        self.resize(600, 800)
        self.setWindowTitle("Calculator")
        iconDir = QtCore.QFileInfo("./img/icon/int_128x128.ico").absoluteFilePath()
        # iconDir = QtCore.QFileInfo("./img/int.png").absoluteFilePath()
        self.setWindowIcon(QIcon(iconDir))

    def initMenu(self):
        self.menuBar = QMenuBar()
        self.editMenu = QMenu("Edit")
        self.helpMenu = QMenu("Help")

        self.menuBar.addMenu(self.editMenu)
        self.menuBar.addMenu(self.helpMenu)

        self.undoAct = QAction("undo")
        self.redoAct = QAction("redo")
        self.docsAct = QAction("docs")

        self.editMenu.addAction(self.undoAct)
        self.editMenu.addAction(self.redoAct)
        self.helpMenu.addAction(self.docsAct)

    def initTabBar(self):
        self.tabBar = QTabWidget()

        self.initTabDiff()
        self.initTabInteg()
        self.initTabLimit()

        self.tabBar.addTab(self.widgetDiff, "Derivation")
        self.tabBar.addTab(self.widgetInteg, "Integral")
        self.tabBar.addTab(self.widgetLimit, "Limit")

    def initTabDiff(self):
        self.widgetDiff = QWidget()

        self.editDiffInput = QLineEdit()
        self.editDiffInput.setPlaceholderText("Input")

        self.labelDiffSymbols = QLabel("Symbols")
        self.editDiffSymbols = QLineEdit()

        self.editDiffSeq = QLineEdit()
        self.labelDiffSeq = QLabel("Derivation Symbol Sequence")

        self.buttonDiff = QPushButton("Derivate")

        self.layoutDiff = QGridLayout()

        self.layoutDiff.addWidget(self.editDiffInput, 0, 0, 1, 8)
        self.layoutDiff.addWidget(self.labelDiffSymbols, 2, 0, 1, 4)
        self.layoutDiff.addWidget(self.labelDiffSeq, 2, 4, 1, 4)
        self.layoutDiff.addWidget(self.editDiffSymbols, 3, 0, 1, 4)
        self.layoutDiff.addWidget(self.editDiffSeq, 3, 4, 1, 4)
        self.layoutDiff.addWidget(self.buttonDiff, 4, 0, 1, 8)
        
        self.layoutDiff.setAlignment(self.buttonDiff, QtCore.Qt.AlignCenter)

        self.widgetDiff.setLayout(self.layoutDiff)

    def initTabInteg(self):
        self.widgetInteg = QWidget()

        self.editIntegInput = QLineEdit()
        self.editIntegInput.setPlaceholderText("Input")

        self.labelIntegSymbols = QLabel("Symbols")
        self.editIntegSymbols = QLineEdit()

        self.editIntegRange = QLineEdit()
        self.labelIntegRange = QLabel("Integral Range")

        self.buttonInteg = QPushButton("Integrate")

        self.layoutInteg = QGridLayout()

        self.layoutInteg.addWidget(self.editIntegInput, 0, 0, 1, 8)
        self.layoutInteg.addWidget(self.labelIntegSymbols, 2, 0, 1, 4)
        self.layoutInteg.addWidget(self.labelIntegRange, 2, 4, 1, 4)
        self.layoutInteg.addWidget(self.editIntegSymbols, 3, 0, 1, 4)
        self.layoutInteg.addWidget(self.editIntegRange, 3, 4, 1, 4)
        self.layoutInteg.addWidget(self.buttonInteg, 4, 0, 1, 8)

        self.layoutInteg.setAlignment(self.buttonInteg, QtCore.Qt.AlignCenter)

        self.widgetInteg.setLayout(self.layoutInteg)

    def initTabLimit(self):
        self.widgetLimit = QWidget()

        self.editLimitInput = QLineEdit()
        self.editLimitInput.setPlaceholderText("Input")

        self.labelLimitSymbols = QLabel("Symbols")
        self.editLimitSymbols = QLineEdit()

        self.editLimitVal = QLineEdit()
        self.labelLimitRange = QLabel("Limit")

        self.buttonLimit = QPushButton("Limit")

        self.layoutLimit = QGridLayout()

        self.layoutLimit.addWidget(self.editLimitInput, 0, 0, 1, 8)
        self.layoutLimit.addWidget(self.labelLimitSymbols, 2, 0, 1, 4)
        self.layoutLimit.addWidget(self.labelLimitRange, 2, 4, 1, 4)
        self.layoutLimit.addWidget(self.editLimitSymbols, 3, 0, 1, 4)
        self.layoutLimit.addWidget(self.editLimitVal, 3, 4, 1, 4)
        self.layoutLimit.addWidget(self.buttonLimit, 4, 0, 1, 8)

        self.layoutLimit.setAlignment(self.buttonLimit, QtCore.Qt.AlignCenter)

        self.widgetLimit.setLayout(self.layoutLimit)

    def initView(self):
        self.sceneRes = QGraphicsScene()
        self.viewRes = QGraphicsView()

        self.viewRes.setScene(self.sceneRes)

        self.viewRes.show()

    def setCanvas(self):
        self.resLatexCanvas = pltView.latexView(width=self.viewRes.width()/100,
                                                height=self.viewRes.height()/100)
        self.sceneRes.addWidget(self.resLatexCanvas)

        self.viewRes.show()

    def layoutMgnt(self):
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.menuBar, 0)
        self.layout.addWidget(self.tabBar, 2)
        self.layout.addWidget(self.viewRes, 4)

        self.setLayout(self.layout)

    def initDocs(self):
        self.widgetDocs = QWidget()
        self.layoutDocs = QVBoxLayout()

        self.webDocs = QWebEngineView()
        self.webDocs.resize(1200, 1600)
        self.webDocs.setZoomFactor(2)
        
        fileDir = QtCore.QFileInfo("./docs/docs.html").absoluteFilePath()
        # print(fileDir)
        self.webDocs.load(QtCore.QUrl("file:///" + fileDir))

        self.layoutDocs.addWidget(self.webDocs)
        self.widgetDocs.setLayout(self.layoutDocs)

    def showDocs(self):
        self.widgetDocs.show()
