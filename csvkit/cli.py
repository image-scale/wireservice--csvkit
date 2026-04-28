#!/usr/bin/env python

"""
Column identifier parsing utilities.
"""

import re

from csvkit.exceptions import ColumnIdentifierError


def parse_column_identifiers(ids, column_names, column_offset=1, excluded_columns=None):
    """
    Parse a comma-separated list of column indices and names into a list of integer indices.

    Supports:
    - Column names: 'name', 'i_work_here'
    - Numeric indices: '1', '2' (1-based by default)
    - Ranges: '1:3', '2-4' (inclusive)
    - Open-ended ranges: ':3', '4:'

    Args:
        ids: Comma-separated string of column identifiers
        column_names: List of column header names
        column_offset: 1 for 1-based indexing (default), 0 for 0-based
        excluded_columns: Comma-separated string of columns to exclude from result

    Returns:
        List of column indices (0-based)
    """
    if not ids:
        return []

    # Parse excluded columns first
    excluded = set()
    if excluded_columns:
        for col in excluded_columns.split(','):
            col = col.strip()
            if col:
                try:
                    idx = match_column_identifier(column_names, col, column_offset)
                    excluded.add(idx)
                except ColumnIdentifierError:
                    # Ignore unknown excluded columns
                    pass

    columns = []

    for part in ids.split(','):
        part = part.strip()
        if not part:
            continue

        # Check for range notation
        # : is always a range separator
        # - is only a range separator if it's between two numbers (e.g., '2-4')
        range_match = None
        if ':' in part:
            range_match = re.match(r'^(\d*):(\d*)$', part)
        elif '-' in part:
            # Only treat hyphen as range if the pattern is like '2-4'
            range_match = re.match(r'^(\d+)-(\d+)$', part)

        if range_match:
            start_str = range_match.group(1)
            end_str = range_match.group(2)

            # Determine start and end
            if start_str == '':
                start = 0
            else:
                start = int(start_str) - column_offset

            if end_str == '':
                end = len(column_names) - 1
            else:
                end = int(end_str) - column_offset

            # Add all columns in range
            for i in range(start, end + 1):
                if i not in excluded:
                    columns.append(i)
        else:
            # Single column identifier
            idx = match_column_identifier(column_names, part, column_offset)
            if idx not in excluded:
                columns.append(idx)

    return columns


def match_column_identifier(column_names, c, column_offset=1):
    """
    Determine what column a single column identifier (name or index) refers to.

    Args:
        column_names: List of column header names
        c: Column identifier (string name or numeric index)
        column_offset: 1 for 1-based indexing (default), 0 for 0-based

    Returns:
        0-based column index
    """
    # If it's an integer, use it directly
    if isinstance(c, int):
        return c - column_offset

    # If it's a string that looks like a number, treat it as a positional index
    c_str = str(c)
    if re.match(r'^-?\d+$', c_str):
        return int(c_str) - column_offset

    # Otherwise look up by name
    try:
        return column_names.index(c_str)
    except ValueError:
        raise ColumnIdentifierError("Column '%s' is invalid. It is neither an integer nor a column name.", c_str)


def normalize_column_type(t):
    """
    Normalize a column type.
    """
    return t
