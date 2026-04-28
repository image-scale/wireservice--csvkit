#!/usr/bin/env python

"""
csvjoin: Join CSV files on a common column.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class CSVJoin(CSVKitUtility):
    description = 'Execute a SQL-like join to merge CSV files on a specified column or columns.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    CSVJoin.launch_new_instance()
