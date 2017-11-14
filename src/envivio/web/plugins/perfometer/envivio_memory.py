#!/usr/bin/python
# -*- coding: utf-8; py-indent-offset: 4 -*-
#  _______ __   _ ____     __
# |       |  \ | |___ \   / /
# |       |   \| | __) | / /-,_
# |       | |\   |/ __/ /__   _|
# |_______|_| \__|_____|   |_|
#
# @author Markus Birth <markus.birth@weltn24.de>

def perfometer_envivio_memory(row, check_command, perfdata):
    if len(perfdata) < 1:
        return "", ""

    phys_used  = int(perfdata[0][1])
    phys_total = int(perfdata[1][1])
    page_used  = int(perfdata[3][1])
    page_total = int(perfdata[4][1])
    virt_used  = int(perfdata[6][1])
    virt_total = int(perfdata[7][1])

    phys_free = phys_total - phys_used
    page_free = page_total - page_used
    virt_free = virt_total - virt_used

    mem_used  = phys_used + page_used + virt_used
    mem_total = phys_total + page_total + virt_total

    # paint used ram and swap
    bar  = '<table><tr>'
    bar += perfometer_td(100 * phys_used / mem_total, "#097054")
    bar += perfometer_td(100 * page_used / mem_total, "#6599ff")
    bar += perfometer_td(100 * virt_used / mem_total, "#ffde00")

    bar += perfometer_td(100 * phys_free / mem_total, "#ccfff1")
    bar += perfometer_td(100 * page_free / mem_total, "#e6eeff")
    bar += perfometer_td(100 * virt_free / mem_total, "#fff8cc")

    bar += "</tr></table>"
    return "%.1f%%" % (100.0 * (float(mem_used) / float(mem_total))), bar

perfometers["check_mk-envivio_memory"] = perfometer_envivio_memory
