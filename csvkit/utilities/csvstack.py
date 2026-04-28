#!/usr/bin/env python

"""
csvstack: Stack multiple CSV files vertically.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class CSVStack(CSVKitUtility):
    description = 'Stack up the rows from multiple CSV files, optionally adding a grouping value.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    CSVStack.launch_new_instance()
