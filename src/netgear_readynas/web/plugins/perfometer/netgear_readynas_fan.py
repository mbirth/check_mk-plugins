#!/usr/bin/python
# -*- coding: utf-8; py-indent-offset: 4 -*-
#  _______ __   _ ____     __
# |       |  \ | |___ \   / /
# |       |   \| | __) | / /-,_
# |       | |\   |/ __/ /__   _|
# |_______|_| \__|_____|   |_|
#
# @author Markus Birth <markus.birth@weltn24.de>

def perfometer_netgear_readynas_fan(row, check_command, perfdata):
    if len(perfdata) < 1:
        return "", ""

    rpm  = float(perfdata[0][1])
    warn = float(perfdata[0][3])
    crit = float(perfdata[0][4])

    if rpm >= crit:
        color = "#d23"
    elif rpm >= warn:
        color = "#dd2"
    else:
        color = "#2d3"

    return "%i rpm" % rpm, perfometer_linear(100*rpm/crit, color)

perfometers["check_mk-netgear_readynas_fan"] = perfometer_netgear_readynas_fan
