#!/usr/bin/env python

"""
csvgrep: Search CSV files.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class CSVGrep(CSVKitUtility):
    description = 'Search CSV files. Like the Unix "grep" command, but for tabular data.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    CSVGrep.launch_new_instance()
