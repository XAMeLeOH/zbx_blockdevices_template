#!/usr/bin/python
# -*- coding: UTF-8 -*-


import json
import os
import subprocess as sp
import sys


LSBLKPATH='/bin/lsblk'
LSBLKARGS='-rdno NAME,TYPE,SIZE'


def main():
    data = []
    p = sp.Popen([LSBLKPATH] + LSBLKARGS.split(" "), stdout=sp.PIPE)
    stdout, stderr = p.communicate()
    for i, line in enumerate(stdout.split("\n")):
        line = line.strip()
        if line == "":
            continue
        fields = line.split(" ")
        if len(fields) != 3:
            continue
        name, tp, sz = fields
        if tp != "disk":
            continue
        if sz == "":
            continue
        data.append({
            "{#DEVINDEX}": i,
            "{#DEVNAME}": name,
            "{#DEVPATH}": "/dev/"+name,
        })
    print json.dumps({"data": data})


if __name__ == "__main__":
    main()
