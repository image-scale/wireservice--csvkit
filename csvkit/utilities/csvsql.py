#!/usr/bin/env python

"""
csvsql: Generate SQL statements for a CSV file or execute those statements directly on a database.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class CSVSQL(CSVKitUtility):
    description = 'Generate SQL statements for one or more CSV files, or execute those statements directly on a database.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    CSVSQL.launch_new_instance()
