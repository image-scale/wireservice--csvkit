#!/usr/bin/env python

"""
csvformat: Convert a CSV file to a custom output format.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class CSVFormat(CSVKitUtility):
    description = 'Convert a CSV file to a custom output format.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    CSVFormat.launch_new_instance()
