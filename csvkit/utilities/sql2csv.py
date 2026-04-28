#!/usr/bin/env python

"""
sql2csv: Execute a SQL query on a database and output the result to a CSV file.
"""

from csvkit.utilities.csvutil import CSVKitUtility


class SQL2CSV(CSVKitUtility):
    description = 'Execute a SQL query on a database and output the results to a CSV file.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def add_arguments(self):
        raise NotImplementedError

    def main(self):
        raise NotImplementedError


def launch_new_instance():
    SQL2CSV.launch_new_instance()
