#!/usr/bin/python
# -*- coding: utf-8; py-indent-offset: 4 -*-
#  _______ __   _ ____     __
# |       |  \ | |___ \   / /
# |       |   \| | __) | / /-,_
# |       | |\   |/ __/ /__   _|
# |_______|_| \__|_____|   |_|
#
# @author Markus Birth <markus.birth@weltn24.de>

def perfometer_selenio_mcp_temp(row, check_command, perfdata):
    if len(perfdata) < 1:
        return "", ""

    tcur = int(perfdata[0][1])
    tmax = int(perfdata[0][6])

    return "%i℃" % tcur, perfometer_linear(tcur*100/tmax, "#f82")

perfometers["check_mk-selenio_mcp_temp"] = perfometer_selenio_mcp_temp
