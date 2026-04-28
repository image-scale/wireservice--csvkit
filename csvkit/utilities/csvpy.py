#!/usr/bin/env python

"""
csvpy: Execute Python code with access to a CSV file as a reader or agate table.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class CSVPy(CSVKitUtility):
    description = 'Load a CSV file into a Python interactive environment.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    CSVPy.launch_new_instance()
