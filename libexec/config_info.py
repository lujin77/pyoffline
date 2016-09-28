#!/usr/bin/env python

import argparse
import sys

from pyoffline import *


if "__main__" == __name__:
    # Set argument parser.
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--parameter", help="config parameter name.")
    args = parser.parse_args()

    with open("config.json", "r") as f:
        config = json.load(f)

    if args.parameter == "py_versions":
        py_versions = config["py_versions"]
        for pyv in py_versions:
            print(pyv)

    elif args.parameter == "essential_packages":
        essential_packages = config["essential_packages"]
        for p in essential_packages:
            print(p)

    else:
        msg = "Unknown config parameter: {}".format(args.parameter)
        sys.exit(msg)

