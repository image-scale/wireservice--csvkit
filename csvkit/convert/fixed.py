#!/usr/bin/env python

"""
Functions for converting fixed-width files to CSV.
"""


def fixed2csv(f, schema, output=None, skip_lines=0):
    """
    Convert a fixed-width file to CSV.
    """
    raise NotImplementedError


class SchemaDecoder:
    """
    Decodes a schema row and tracks column positions.
    """

    def __init__(self, header):
        raise NotImplementedError

    def __call__(self, row):
        raise NotImplementedError


class FixedWidthRowParser:
    """
    Parses rows from a fixed-width file based on a schema.
    """

    def __init__(self, schema_file):
        raise NotImplementedError

    def parse(self, line):
        raise NotImplementedError
