#!/usr/bin/env python

"""
csvclean: Cleans a CSV file of common errors.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class CSVClean(CSVKitUtility):
    description = 'Fix common errors in a CSV file.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    CSVClean.launch_new_instance()
