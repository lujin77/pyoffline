#!/usr/bin/env python

from pyoffline import *

if "__main__" == __name__:
    with open("config.json", "r") as f:
        config = json.load(f)

    py_versions = config["py_versions"]

    for py_version in py_versions:
        print(py_version)

