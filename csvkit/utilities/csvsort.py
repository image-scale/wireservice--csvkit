#!/usr/bin/env python

"""
csvsort: Sort CSV files.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class CSVSort(CSVKitUtility):
    description = 'Sort CSV files. Like the Unix "sort" command, but for tabular data.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    CSVSort.launch_new_instance()
