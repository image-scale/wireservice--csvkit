#!/usr/bin/env python

"""
Column identifier parsing utilities.
"""

from csvkit.exceptions import ColumnIdentifierError


def parse_column_identifiers(ids, column_names, column_offset=1, excluded_columns=None):
    """
    Parse a comma-separated list of column indices and names into a list of integer indices.
    """
    raise NotImplementedError


def match_column_identifier(column_names, c, column_offset=1):
    """
    Determine what column a single column identifier (name or index) refers to.
    """
    raise NotImplementedError


def normalize_column_type(t):
    """
    Normalize a column type.
    """
    raise NotImplementedError
