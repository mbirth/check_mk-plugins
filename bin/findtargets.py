#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import os
import sys

if len(sys.argv) < 3:
    print("Syntax: {} BUILD_DIR FILE_LIST".format(sys.argv[0]))
    sys.exit(1)

source_dirs = sys.argv[2:]
dst_dir = sys.argv[1]

for src_dir in source_dirs:
    pkg_name = os.path.basename(src_dir)

    info = {
        "name": pkg_name,
        "version": 1.0
    }

    if os.path.isfile(src_dir + "/baseinfo.ini"):
        cfg = configparser.ConfigParser()
        cfg.read(src_dir + "/baseinfo.ini")
        for key in cfg["info"]:
            info[key] = cfg["info"][key]

    dst_file = os.path.normpath(dst_dir + "/" + "{}-{}.mkp".format(info["name"], info["version"]))
    print(dst_file)
