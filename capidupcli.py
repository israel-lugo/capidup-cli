#! /usr/bin/env python

# CapiDup - quickly find duplicate files in directories
# Copyright (C) 2010,2014,2016 Israel G. Lugo
#
# This file is part of CapiDup.
#
# CapiDup is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# CapiDup is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with CapiDup. If not, see <http://www.gnu.org/licenses/>.
#
# For suggestions, feedback or bug reports: israel.lugo@lugosys.com


"""Quickly find duplicate files in directories.

CapiDup recursively crawls through all the files in a list of directories
and identifies duplicate files. Duplicate files are files with the exact
same content, regardless of their name, location or timestamp.

This program is designed to be quite fast. It uses a smart algorithm to
detect and group duplicate files using a single pass on each file (that is,
CapiDup doesn't need to compare each file to every other).

This module implements the CLI interface. The actual functionality is in
the capidup package.

"""


# In the packaged version, this module is imported from a standalone "shim"
# script, automatically generated by setuptools. The script calls main(),
# which is defined as an entry point in setup.py.


# be compatible with Python 3
from __future__ import print_function

import sys
import argparse

import capidup.finddups as finddups


__version__ = "1.0.0"


__all__ = [ 'main' ]


def parse_args():
    """Parse command-line arguments.

    Returns a populated namespace with all arguments and their values.

    """
    parser = argparse.ArgumentParser(
            description="Quickly find duplicate files in directories.")

    parser.add_argument('directories', nargs='+', metavar='directory', help="where to scan for duplicates")

    # This doesn't show license information, a la GNU. Would be nice.
    # Create a custom Action that prints what we want and exits?  Can't
    # place everything in "version" string, because the default formatter
    # wraps everything.
    parser.add_argument('-V', '--version', action='version', version="CapiDup %s" % __version__)

    args = parser.parse_args()

    return args


def main():
    """Main program function."""

    args = parse_args()

    duplicate_files_list, errors = finddups.find_duplicates_in_dirs(args.directories)

    # sort the list of lists of duplicate files, so files in the same
    # directory show up near each other, instead of randomly scattered
    duplicate_files_list.sort()
    for duplicate_files in duplicate_files_list:
        duplicate_files.sort()
        for filename in duplicate_files:
            print(filename)

        print('-' * 30)

    if errors:
        # XXX: Should we print the error strings again, so they are all
        # together in one place?
        sys.stderr.write("error: some files could not be compared\n")
        sys.exit(1)



if __name__ == '__main__':
    main()


# vim: set expandtab smarttab shiftwidth=4 softtabstop=4 tw=75 :
