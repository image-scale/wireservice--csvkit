#!/usr/bin/env python

"""
Functions for cleaning up CSV data.
"""


def join_rows(rows, separator=' '):
    """
    Given a list of rows (lists of cells), merge them into a single row.

    This is used to fix rows that were split due to embedded newlines.
    The first element of each subsequent row is joined to the last element
    of the accumulated result using the separator.

    Args:
        rows: List of rows (each row is a list of cell values)
        separator: String to use when joining cell values (default: ' ')

    Returns:
        A single row (list of cell values)
    """
    if not rows:
        return []

    # Start with a copy of the first row
    result = list(rows[0])

    # Process each subsequent row
    for row in rows[1:]:
        if not row:
            continue

        # Join the first element of this row to the last element of the result
        if result:
            result[-1] = separator.join([result[-1], row[0]])
        else:
            result.append(row[0])

        # Add remaining elements of this row
        result.extend(row[1:])

    return result
