#!/usr/bin/env python

"""
csvlook: Render a CSV file in the console as a Markdown-compatible table.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class CSVLook(CSVKitUtility):
    description = 'Render a CSV file in the console as a Markdown-compatible, fixed-width table.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    CSVLook.launch_new_instance()
