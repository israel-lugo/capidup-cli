
"""Package information for capidup-cli."""

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
    url='https://github.com/israel-lugo/capidup-cli',
    version=find_version([ "capidupcli.py" ]),
    py_modules=[ 'capidupcli' ],
    install_requires=[ 'capidup>=1,<2' ],
    entry_points={
        'console_scripts': [ 'capidup=capidupcli:main' ],
    },
    license='GPLv3+',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities',
    ],
    long_description=read([ "README.rst" ])
)
