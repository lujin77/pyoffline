import json
import os
import subprocess


# Directory contains python interpreter.
_pydir = "py_versions"

# Cpython mirror url.
_pyurl = "http://mirrors.sohu.com/python"
#_pyurl = "https://www.python.org/ftp/python"


def _exec_command(command_list):
    """
    Helper function to execute shell command.
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
    if not os.path.exists(_pydir):
        os.mkdir(_pydir)

    # Download CPython tarball.
    url_template = "{}/{}/Python-{}.tgz"
    download_url = url_template.format(_pyurl, version, version)
    tarname = "{}/Python-{}.tar.gz".format(_pydir, version)

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


if "__main__" == __name__:
    download_cpython("2.7.12")

