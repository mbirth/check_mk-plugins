#!/usr/bin/python
# -*- coding: utf-8; py-indent-offset: 4 -*-
#  _______ __   _ ____     __
# |       |  \ | |___ \   / /
# |       |   \| | __) | / /-,_
# |       | |\   |/ __/ /__   _|
# |_______|_| \__|_____|   |_|
#
# @author Markus Birth <markus.birth@weltn24.de>

def perfometer_snell_iqh_voltage(row, check_command, perfdata):
    if len(perfdata) < 1:
        return "", ""

    vcur = abs(float(perfdata[0][1]))

    return "%.1fV" % vcur, perfometer_linear( (vcur-7.0)*100, "#48f")

perfometers["check_mk-snell_iqh_voltage"] = perfometer_snell_iqh_voltage
