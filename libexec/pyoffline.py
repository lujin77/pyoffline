#!/usr/bin/env python

import logging
import json
import os
import subprocess
import sys

import pip


# Initialize logger.
logger = logging.getLogger("pyoffline")
logger.setLevel(logging.INFO)
_console_hdlr = logging.StreamHandler()
_console_hdlr.setLevel(logging.INFO)
_formatter = logging.Formatter("%(name)s   %(levelname)-8s %(message)s")
_console_hdlr.setFormatter(_formatter)
logger.addHandler(_console_hdlr)


def _exec_command(command_list):
    """
    Execute shell command with instant output on stdout.
    """
    p = subprocess.Popen(command_list, stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()


def get_pyversion():
    """
    Get current python interpreter version.

    Returns:
    --------
    version of python, str. e.g. "2.7.12"
    """
    info = sys.version_info
    version = "{}.{}.{}".format(info.major, info.minor, info.micro)

    return version


def download_cpython(version):
    """
    Download python interpretors from sohu mirror'.

    Parameters:
    -----------
    version: version number of CPython, str.

    """
    # Directory contains python interpreter.
    pydir = "py_versions"

    # Cpython mirror url.
    pyurl = "http://mirrors.sohu.com/python"
    #_pyurl = "https://www.python.org/ftp/python"

    if not os.path.exists(pydir):
        os.mkdir(pydir)

    # Download CPython tarball.
    url_template = "{}/{}/Python-{}.tgz"
    download_url = url_template.format(pyurl, version, version)
    tarname = "{}/Python-{}.tar.gz".format(pydir, version)

    command = ["wget", "-c", download_url, "-O", tarname]
    _exec_command(command)

    return


def download_package(package_name):
    """
    Download python package and its dependencies.

    Parameters:
    -----------
    packages_name: name of python package, str. e.g. "ipython==2.2.0"
    """
    # Name of packages directory.
    packdir = "py_packages"

    # PyPI source url.
    pypi_src = "http://pypi.douban.com/simple"

    # Python version.
    py_version = get_pyversion()

    # Create top packages directory.
    if not os.path.exists(packdir):
        os.mkdir(packdir)

    # Create python version directory.
    pydir = "{}/{}".format(packdir, py_version)
    if not os.path.exists(pydir):
        os.mkdir(pydir)

    # Download package.
    command = ["download", "-d", pydir,
               "-i", pypi_src, package_name]
    pip.main(command)

    return

