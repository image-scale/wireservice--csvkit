#!/usr/bin/env python

"""
Conversion utilities for various file formats to CSV.
"""

import os

# Map file extensions to format names
FORMATS = {
    '.csv': 'csv',
    '.dbf': 'dbf',
    '.json': 'json',
    '.geojson': 'geojson',
    '.xls': 'xls',
    '.xlsx': 'xlsx',
}


def guess_format(path):
    """
    Given a file path, guess the format of the file based on its extension.

    Returns the format name (e.g., 'csv', 'xls', 'xlsx', 'json', 'dbf', 'fixed', 'geojson')
    or None if the format is not recognized.
    """
    _, ext = os.path.splitext(path)
    ext = ext.lower()

    if ext in FORMATS:
        return FORMATS[ext]

    # If no extension or unrecognized extension, assume fixed-width
    if not ext:
        return 'fixed'

    return None
