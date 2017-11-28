#!/usr/bin/python
# -*- coding: utf-8; py-indent-offset: 4 -*-
#  _______ __   _ ____     __
# |       |  \ | |___ \   / /
# |       |   \| | __) | / /-,_
# |       | |\   |/ __/ /__   _|
# |_______|_| \__|_____|   |_|
#
# @author Markus Birth <markus.birth@weltn24.de>

def perfometer_mayah_c12_fan(row, check_command, perfdata):
    if len(perfdata) < 1:
        return "", ""

    rpm  = float(perfdata[0][1])
    if perfdata[0][3]:
        warn = float(perfdata[0][3])
    else:
        warn = 7000
    if perfdata[0][4]:
        crit = float(perfdata[0][4])
    else:
        crit = 8500

    if rpm >= crit:
        color = "#d23"
    elif rpm >= warn:
        color = "#dd2"
    else:
        color = "#2d3"

    return "%i rpm" % rpm, perfometer_linear(100*rpm/crit, color)

perfometers["check_mk-mayah_c12_fan"] = perfometer_mayah_c12_fan
