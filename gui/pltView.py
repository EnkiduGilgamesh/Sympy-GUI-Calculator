# -*- python 3.8.10 -*-
# -*- coding:utf-8 -*-
####################################################################################################
# File: \pltView.py                                                                                #
# Project: gui                                                                                     #
# Created Date: Saturday Oct 30th 2021, 10:39:23 am                                                #
# Author: Wenren Muyan                                                                             #
# Comments: make a canvas through matplotlib for QgraphicsScene                                    #
# --------------------------------------------------------------------------------                 #
# Last Modified: 30/10/2021 11:25:19                                                               #
# Modified By: Wenren Muyan                                                                        #
# --------------------------------------------------------------------------------                 #
# Copyright (c) 2021 - future Wenren Muyan                                                         #
# --------------------------------------------------------------------------------                 #
# HISTORY:                                                                                         #
# Date				By				Comments                                                       #
# --------------------------------------------------------------------------------                 #
####################################################################################################


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt


class latexView(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=10, height=5, dpi=100):
        fig = plt.Figure(figsize=(width, height), dpi=dpi, tight_layout=True)

        super(latexView, self).__init__(fig)

        self.axes = fig.add_subplot(111)
        self.axesConfig()

    def axesConfig(self):  # Remove the axis
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)
        self.axes.xaxis.set_ticks([])
        self.axes.yaxis.set_ticks([])
        self.axes.set_xlim((-2, 2))
        self.axes.set_ylim((-2, 2))

    def dispalyRes(self, latex_cmd=""):
        self.axes.clear()
        self.axesConfig()
        self.axes.text(-2, 1, r'${}$'.format(latex_cmd), style="italic", fontsize=25)
        self.draw()
