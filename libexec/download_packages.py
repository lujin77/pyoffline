#!/usr/bin/env python

from pyoffline import *


if "__main__" == __name__:
    # Open config file.
    with open("config.json", "r") as f:
        config = json.load(f)

    py_packages = config["py_packages"]
    essential_packages = config["essential_packages"]

    # Download packages.
    py_version = get_pyversion()
    if py_version not in py_packages:
        raise ValueError("Python-{} not found in config.json.")

    packages = py_packages[py_version]
    for package in packages:
        logger.info("Downloading {} for Python-{}...".format(package, py_version))
        download_package(package)

    # Download virtualenv.
    for essential_require in essential_packages:

        # Ignore same downloaded packages.
        ignore = False
        for downloaded in packages:
            if downloaded.startswith(essential_require):
                ignore = True
                break
        if ignore:
            msg = "Ignore {}, {} has been downloaded before"
            logger.warning(msg.format(essential_require, downloaded))
            continue

        download_package(package)

