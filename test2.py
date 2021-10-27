# -*- python 3.8.10 -*-
# -*- coding:utf-8 -*-
####################################################################################################
# File: \test2.py                                                                                  #
# Project: Calculator                                                                              #
# Created Date: Wednesday Oct 27th 2021, 9:24:28 am                                                #
# Author: Wenren Muyan                                                                             #
# Comments:                                                                                        #
# --------------------------------------------------------------------------------                 #
# Last Modified: 27/10/2021 10:44:53                                                               #
# Modified By: Wenren Muyan                                                                        #
# --------------------------------------------------------------------------------                 #
# Copyright (c) 2021 - future Wenren Muyan                                                         #
# --------------------------------------------------------------------------------                 #
# HISTORY:                                                                                         #
# Date				By				Comments                                                       #
# --------------------------------------------------------------------------------                 #
####################################################################################################


#import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)

# Set titles for the figure and the subplot respectively
# plt.title(r'$\alpha > \beta$')
fig.suptitle(r'$\mathtt{\int_0^1 f(x)dx}$ $\frac{1}{x_2}$', fontsize=14)
ax.set_title('axes title')

ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

# Set both x- and y-axis limits to [0, 10] instead of default [0, 1]
ax.axis([0, 10, 0, 10])

ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

ax.text(3, 2, 'unicode: Institut für Festkörperphysik')

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)

ax.plot([2], [1], 'o')
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()
