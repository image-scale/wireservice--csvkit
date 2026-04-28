#!/usr/bin/env python

"""
csvcut: Filter and truncate CSV files.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class CSVCut(CSVKitUtility):
    description = 'Filter and truncate CSV files. Like the Unix "cut" command, but for tabular data.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    CSVCut.launch_new_instance()
