#!/usr/bin/python
# -*- coding: utf-8; py-indent-offset: 4 -*-
#  _______ __   _ ____     __
# |       |  \ | |___ \   / /
# |       |   \| | __) | / /-,_
# |       | |\   |/ __/ /__   _|
# |_______|_| \__|_____|   |_|
#
# @author Markus Birth <markus.birth@weltn24.de>

def perfometer_snell_iqh_cpu(row, check_command, perfdata):
    if len(perfdata) < 1:
        return "", ""

    ccur = int(perfdata[0][1])
    #cwarn = int(perfdata[0][2])
    #ccrit = int(perfdata[0][3])

    cwarn = 95
    ccrit = 98

    if ccur > ccrit:
        color = "#f88"
    elif ccur > cwarn:
        color = "#ff6"
    else:
        color = "#8f8"

    return "%i%%" % ccur, perfometer_linear(ccur, color)

perfometers["check_mk-snell_iqh_cpu"] = perfometer_snell_iqh_cpu
