#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import json
import os
import sys
import pprint
import subprocess
import tarfile
import time
from io import BytesIO

if len(sys.argv) < 3:
    print("Syntax: {} SRCDIR DESTDIR".format(sys.argv[0]))
    sys.exit(1)

src_dir = sys.argv[1]
dst_dir = sys.argv[2]

if not os.path.isdir(src_dir):
    print("{} is not a directory!".format(src_dir))
    sys.exit(2)

if not os.path.isdir(dst_dir):
    print("{} is not a directory!".format(dst_dir))
    sys.exit(3)

pkg_name = os.path.basename(src_dir)

info = {
    "title"                : "Title of {}".format(pkg_name),
    "name"                 : pkg_name,
    "description"          : "Please add a description here",
    "version"              : "1.0",
    "version.packaged"     : "1.4.0",
    "version.min_required" : "1.4.0",
    "packaged_by"          : "makemkp.py",
    "author"               : "Add your name here",
    "download_url"         : "http://example.com/{}/".format(pkg_name),
    "files"                : {}
}

cfg = configparser.ConfigParser()
cfg.read(src_dir + "/baseinfo.ini")

for key in cfg["info"]:
    info[key] = cfg["info"][key]

dst_file = os.path.normpath(dst_dir + "/" + "{}-{}.mkp".format(info["name"], info["version"]))

print("Packaging {} v{} into {}...".format(info["name"], info["version"], dst_file))

tar = tarfile.open(name=dst_file, mode="w:gz")


# COLLECT FILES

package_parts = [ (part, title, perm) for part, title, perm in [
  ( "checks",        "Checks",               0o644 ),
  ( "notifications", "Notification scripts", 0o755 ),
  ( "inventory",     "Inventory plugins",    0o644 ),
  ( "checkman",      "Checks' man pages",    0o644 ),
  ( "agents",        "Agents",               0o755 ),
  ( "web",           "Multisite extensions", 0o644 ),
  ( "pnp-templates", "PNP4Nagios templates", 0o644 ),
  ( "doc",           "Documentation files",  0o644 ),
  ( "bin",           "Binaries",             0o755 ),
  ( "lib",           "Libraries",            0o644 ),
#  ( "mibs",          "SNMP MIBs",            0o644 ),
]]

def files_in_dir(dir, prefix = ""):
    if dir == None or not os.path.exists(dir):
        return []

    result = []
    files = os.listdir(dir)
    for f in files:
        if f in [ '.', '..' ] or f.startswith('.') or f.endswith('~'):
            continue

        path = dir + "/" + f
        if os.path.isdir(path):
            result += files_in_dir(path, prefix + f + "/")
        else:
            result.append(prefix + f)
    result.sort()
    return result

def create_tar_info(filename, size):
    info = tarfile.TarInfo()
    info.mtime = time.time()
    info.uid = 0
    info.gid = 0
    info.size = size
    info.mode = 0o644
    info.type = tarfile.REGTYPE
    info.name = filename
    return info

def tar_from_string(tar, filename, payload):
    data_stream = BytesIO(payload)
    tarinfo = create_tar_info(filename, len(data_stream.getvalue()))
    tar.addfile(tarinfo, data_stream)

files = {}
num_files = 0
for part, title, perm in package_parts:
    files_list = files_in_dir(src_dir + "/" + part)
    files[part] = files_list
    num_files += len(files_list)

info["files"] = files
info["num_files"] = num_files

info_file = pprint.pformat(info)
info_json = json.dumps(info)
tar_from_string(tar, "info", info_file.encode("utf-8"))
tar_from_string(tar, "info.json", info_json.encode("utf-8"))


for part in info["files"]:
    filenames = info["files"][part]
    if len(filenames) > 0:
        subtarname = part + ".tar"
        subdata = subprocess.check_output(["tar", "cf", "-", "--dereference", "--force-local",
                                           "-C", src_dir + "/" + part] + filenames)
        tar_from_string(tar, subtarname, subdata)

tar.close()
