#!/usr/bin/env python

"""
in2csv: Convert various tabular data formats to CSV.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class In2CSV(CSVKitUtility):
    description = 'Convert common, but less awesome, tabular data formats to CSV.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    In2CSV.launch_new_instance()
