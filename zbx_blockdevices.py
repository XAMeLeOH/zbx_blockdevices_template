#!/usr/bin/python
# -*- coding: UTF-8 -*-


import json
import os
import subprocess as sp
import sys


LSBLKPATH='/bin/lsblk'
LSBLKARGS='-rdno NAME,RM'


def main():
    data = []
    p = sp.Popen([LSBLKPATH] + LSBLKARGS.split(" "), stdout=sp.PIPE)
    stdout, stderr = p.communicate()
    for i, line in enumerate(stdout.split("\n")):
        line = line.strip()
        if line == "":
            continue
        fields = line.split(" ")
        if len(fields) != 2:
            raise Exception("Unknown fields in lsblk output")
        name, rm = fields
        if int(rm) != 0:
            continue
        data.append({
            "{#DEVINDEX}": i,
            "{#DEVNAME}": name,
            "{#DEVPATH}": "/dev/"+name,
        })
    print json.dumps({"data": data})


if __name__ == "__main__":
    main()


