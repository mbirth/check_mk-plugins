#!/usr/bin/python
# -*- coding: utf-8; py-indent-offset: 4 -*-
#  _______ __   _ ____     __
# |       |  \ | |___ \   / /
# |       |   \| | __) | / /-,_
# |       | |\   |/ __/ /__   _|
# |_______|_| \__|_____|   |_|
#
# @author Markus Birth <markus.birth@weltn24.de>

def perfometer_snell_iqh_power(row, check_command, perfdata):
    if len(perfdata) < 1:
        return "", ""

    pcur = int(perfdata[0][1])
    pmax = int(perfdata[0][6])

    percent = float(pcur)*100.0/float(pmax)

    return "%i%%" % percent, perfometer_linear(percent, "#66a")

perfometers["check_mk-snell_iqh_power"] = perfometer_snell_iqh_power
