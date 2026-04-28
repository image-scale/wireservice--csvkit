#!/usr/bin/env python

"""
csvjson: Convert a CSV file to JSON.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class CSVJSON(CSVKitUtility):
    description = 'Convert a CSV file into JSON (or GeoJSON).'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    CSVJSON.launch_new_instance()
