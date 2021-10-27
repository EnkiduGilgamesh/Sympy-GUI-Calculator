# -*- python 3.8.10 -*-
# -*- coding:utf-8 -*-
####################################################################################################
# File: \test3.py                                                                                  #
# Project: Calculator                                                                              #
# Created Date: Wednesday Oct 27th 2021, 3:28:22 pm                                                #
# Author: Wenren Muyan                                                                             #
# Comments:                                                                                        #
# --------------------------------------------------------------------------------                 #
# Last Modified: 27/10/2021 04:22:16                                                               #
# Modified By: Wenren Muyan                                                                        #
# --------------------------------------------------------------------------------                 #
# Copyright (c) 2021 - future Wenren Muyan                                                         #
# --------------------------------------------------------------------------------                 #
# HISTORY:                                                                                         #
# Date				By				Comments                                                       #
# --------------------------------------------------------------------------------                 #
####################################################################################################


from PySide2.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QVBoxLayout, QApplication

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class figureCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=10, height=5, xlim=(0, 2500), ylim=(-2, 2), dpi=100):
        self.fig = plt.Figure(figsize=(width, height), dpi=dpi, tight_layout=True)

        super(figureCanvas, self).__init__(self.fig)

        self.axes = self.fig.add_subplot(111)

        self.axes.set_title(r"hello")

        self.axes.spines['top'].set_visible(False)  # 去掉上面的横线
        self.axes.spines['right'].set_visible(False)
        self.axes.set_xlim(xlim)
        self.axes.set_ylim(ylim)


class myWidget(QWidget):
    def __init__(self, parent=None):
        super(myWidget, self).__init__(parent)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView()

        self.figure = figureCanvas(width=self.view.width()/100, \
                              height=self.view.height()/100)
        
        self.scene.addWidget(self.figure)
        self.view.setScene(self.scene)

        self.figure.draw()
        self.view.show()

        self.scene2 = QGraphicsScene()
        self.view2 = QGraphicsView()

        self.figure2 = figureCanvas(width=self.view.width()/100, \
                              height=self.view.height()/100)
        
        self.scene2.addWidget(self.figure2)
        self.view2.setScene(self.scene2)

        self.figure2.draw()
        self.view2.show()

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.view)
        self.layout.addWidget(self.view2)

        self.setLayout(self.layout)


app = QApplication()

main_window = myWidget()
main_window.show()

app.exec_()
