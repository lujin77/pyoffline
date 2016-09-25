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


def download_package(package_name, py_version):
    """
    Download python package and its dependencies.

    Parameters:
    -----------
    packages_name: name of python package, str. e.g. "ipython==2.2.0"
    py_version: version of python interpreter, str. e.g. "3.5.2"
    """
    # Name of packages directory.
    packdir = "py_packages"

    # PyPI source url.
    pypi_src = "http://pypi.douban.com/simple"

    # Create top packages directory.
    if not os.path.exists(packdir):
        os.mkdir(packdir)

    # Create python version directory.
    pydir = "{}/{}".format(packdir, py_version)
    if not os.path.exists(pydir):
        os.mkdir(pydir)

    # Create sub directories.
    subdir = "{}/{}".format(pydir, package_name)
    if not os.path.exists(subdir):
        os.mkdir(subdir)

    # Download package.
    command = ["download", "-d", subdir,
               "-i", pypi_src, package_name]
    pip.main(command)

    return


if "__main__" == __name__:
    # Read configuration file.
#    with open("config.json", "r") as f:
#        config = json.load(f)
#
#    py_versions = config["py_versions"]
#    py_packages = config["py_packages"]
     download_package('vaspy', '2.7.12')

