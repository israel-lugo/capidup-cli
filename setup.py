
"""Package information for capidup."""

import os.path
import io
import re

from setuptools import setup


def read(file_path_components, encoding="utf8"):
    """Read the contents of a file.

    Receives a list of path components to the file and joins them in an
    OS-agnostic way. Opens the file for reading using the specified
    encoding, and returns the file's contents.

    Works both in Python 2 and Python 3.

    """
    with io.open(
        os.path.join(os.path.dirname(__file__), *file_path_components),
        encoding=encoding
    ) as fp:
        return fp.read()


def find_version(file_path_components):
    """Grep the specified file for the version number.

    Receives a list of path components to the file and joins them in an
    OS-agnostic way. Reads the file's contents and extracts the version
    number, from a line like:

        __version__ = "xxx"

    """
    version_file = read(file_path_components)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='capidup-cli',
    description='Quickly find duplicate files in directories (CLI utility)',
    author="Israel G. Lugo",
    author_email='israel.lugo@lugosys.com',
    version=find_version([ "capidupcli.py" ]),
    py_modules=[ 'capidupcli' ],
    install_requires=[ 'capidup' ],
    entry_points={
        'console_scripts': [ 'capidup=capidupcli:main' ],
    },
    license='License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    long_description="""
CapiDup recursively crawls through all the files in a list of directories and
identifies duplicate files. Duplicate files are files with the exact same
content, regardless of their name, location or timestamp.

This program is designed to be quite fast. It uses a smart algorithm to detect
and group duplicate files using a single pass on each file (that is, CapiDup
doesn't need to compare each file to every other).

capidup-cli is the command-line utility. It depends on the capidup library
package, which actually implements the functionality.
"""
)
