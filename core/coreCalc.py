# -*- python 3.8.10 -*-
# -*- coding:utf-8 -*-
####################################################################################################
# File: \coreCalc.py                                                                               #
# Project: core                                                                                    #
# Created Date: Friday Oct 29th 2021, 6:58:56 pm                                                   #
# Author: Wenren Muyan                                                                             #
# Comments: calculate limit, integral, and differential                                            #
# --------------------------------------------------------------------------------                 #
# Last Modified: 2/11/2021 11:04:32                                                                #
# Modified By: Wenren Muyan                                                                        #
# --------------------------------------------------------------------------------                 #
# Copyright (c) 2021 - future Wenren Muyan                                                         #
# --------------------------------------------------------------------------------                 #
# HISTORY:                                                                                         #
# Date				By				Comments                                                       #
# 
# 2021-11-2		    WR-MY			complete integrate and limit
# 
# 2021-10-29		WR-MY			complete differential
# --------------------------------------------------------------------------------                 #
####################################################################################################


import re as RE

from sympy import *


class calcCore():
    def __init__(self):
        self.input = [" ", " ", " ", " "]
        # ["lineEdit 1", "lineEdit 2", "lineEdit 3", "lineEdit 4"]
        self.output = " "

    def calcDispatcher(self, editInputStr, slec):
        for i in range(4):
            self.input[i] = editInputStr[i]

        if slec == "Derivate":
            self.calcDiff()
        elif slec == "Integrate":
            self.calcInteg()
        elif slec == "Limit":
            self.calcLimit()
        else:
            return
        
    def calcDiff(self):
        oper_symbols = RE.split(" +", self.input[1])
        for i in range(len(oper_symbols)):
            exec("{} = symbols('{}')".format(oper_symbols[i], oper_symbols[i]))

        diff_seq_symbols = RE.split(" +", self.input[2])

        diff_cmd = "diff({}".format(self.input[0])

        for i in range(len(diff_seq_symbols)):
            diff_cmd += ","
            diff_cmd += diff_seq_symbols[i]
        diff_cmd += ")"
        
        # print(diff_cmd)

        self.output = str(eval("latex({})".format(diff_cmd)))

        # print(self.output)

    def calcInteg(self):
        oper_symbols = RE.split(" +", self.input[1])
        for i in range(len(oper_symbols)):
            exec("{} = symbols('{}')".format(oper_symbols[i], oper_symbols[i]))
        
        integ_seq_symbols = RE.split(" +", self.input[2])

        integ_cmd = "integrate({}".format(self.input[0])

        for i in range(len(integ_seq_symbols)):
            integ_cmd += ","
            integ_cmd += integ_seq_symbols[i]

        integ_cmd += ")"

        # print(integ_cmd)

        self.output = str(eval("latex({})".format(integ_cmd)))

        # print(self.output)

    def calcLimit(self):
        oper_symbols = RE.split(" +", self.input[1])
        for i in range(len(oper_symbols)):
            exec("{} = symbols('{}')".format(oper_symbols[i], oper_symbols[i]))
        
        limit_symbol_value = RE.split(" +", self.input[2])

        limit_cmd = "limit({},{},{})".format(self.input[0], limit_symbol_value[0],
                                             limit_symbol_value[1])

        # print(limit_cmd)

        self.output = str(eval("latex({})".format(limit_cmd)))

        # print(self.output)
