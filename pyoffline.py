import json
import os
import subprocess

import pip


def _exec_command(command_list):
    """
    Execute shell command with instant output on stdout.
    """
    p = subprocess.Popen(command_list, stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()


def download_cpython(version):
    """
    Download python interpretors from https://python.org.

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

    # Create top packages directories.
    if not os.path.exists(packdir):
        os.mkdir(packdir)

    # Create sub directories.
    subdir = "{}/{}".format(packdir, package_name)
    if not os.path.exists(subdir):
        os.mkdir(subdir)

    # Download package.
    command = ["download", "-d", subdir,
               "-i", pypi_src, package_name]
    pip.main(command)

    return


if "__main__" == __name__:
    download_package("vaspy")
    #download_cpython("2.7.12")

