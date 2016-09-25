#!/usr/bin/env python

from pyoffline import *

if "__main__" == __name__:
    # Read config file.
    with open("config.json", "r") as f:
        config = json.load(f)
    
    py_versions = config["py_versions"]

    # Download pythons.
    for py_version in py_versions:
        logger.info("Downloading Python-{}".format(py_version))
        download_cpython(py_version)

