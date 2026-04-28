#!/usr/bin/env python

"""
csvstat: Print summary statistics for each column in a CSV file.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class CSVStat(CSVKitUtility):
    description = 'Print descriptive statistics for each column in a CSV file.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    CSVStat.launch_new_instance()
