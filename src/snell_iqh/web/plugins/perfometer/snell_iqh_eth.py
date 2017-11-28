#!/usr/bin/python
# -*- coding: utf-8; py-indent-offset: 4 -*-
#  _______ __   _ ____     __
# |       |  \ | |___ \   / /
# |       |   \| | __) | / /-,_
# |       | |\   |/ __/ /__   _|
# |_______|_| \__|_____|   |_|
#
# @author Markus Birth <markus.birth@weltn24.de>

def perfometer_snell_iqh_eth(row, check_command, perfdata):
    if len(perfdata) < 2:
        return "", ""

    tin  = float(perfdata[0][1])
    tout = float(perfdata[1][1])

    text = "%-.1fKB/s&nbsp;&nbsp;&nbsp;%-.1fKB/s" % (tin, tout)

    return text, perfometer_logarithmic_dual(
            tin, "#60e0a0", tout, "#60a0e0", 10, 10)

perfometers["check_mk-snell_iqh_eth"] = perfometer_snell_iqh_eth
