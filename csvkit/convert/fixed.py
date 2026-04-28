#!/usr/bin/env python

"""
Functions for converting fixed-width files to CSV.
"""

import csv
import io

import agate


def fixed2csv(f, schema, output=None, skip_lines=0, **kwargs):
    """
    Convert a fixed-width file to CSV.

    Args:
        f: File-like object containing fixed-width data
        schema: File-like object containing the schema CSV
        output: Optional file-like object for output. If None, returns a string.
        skip_lines: Number of lines to skip at the beginning of the input file
        **kwargs: Additional keyword arguments (ignored)

    Returns:
        If output is None, returns the CSV as a string.
        Otherwise returns empty string and writes to the output file.
    """
    streaming = bool(output)

    if not streaming:
        output = io.StringIO()

    parser = FixedWidthRowParser(schema)

    # Skip lines if requested
    for _ in range(skip_lines):
        f.readline()

    # Write CSV using agate writer
    writer = agate.csv.writer(output)
    writer.writerow(parser.headers)

    for line in f:
        # Strip newline but preserve other whitespace
        line = line.rstrip('\n').rstrip('\r')
        if line:  # Skip empty lines
            row = parser.parse(line)
            writer.writerow(row)

    if not streaming:
        result = output.getvalue()
        output.close()
        return result

    return ''


class SchemaDecoder:
    """
    Decodes a schema row and tracks column positions.

    The schema CSV has columns: column, start, length (in any order).
    """

    def __init__(self, header):
        """
        Initialize the decoder with a header row.

        Args:
            header: List of column names from the schema CSV header
        """
        self.column = header.index('column')
        self.start = header.index('start')
        self.length = header.index('length')
        self.one_based = None  # Will be determined on first row
        self._last_end = 0  # Track the last column end position

    def __call__(self, row):
        """
        Decode a schema row.

        Args:
            row: A list of values from the schema CSV

        Returns:
            Tuple of (column_name, start_position, length)
        """
        column_name = row[self.column]
        start = int(row[self.start])
        length = int(row[self.length])

        # Determine if positions are 0-based or 1-based
        if self.one_based is None:
            # If the first start position equals the last end position, it's 0-based
            # If start == 1 and last_end == 0, it's 1-based
            if start == 1 and self._last_end == 0:
                self.one_based = True
            elif start == 0:
                self.one_based = False
            else:
                # Default to 0-based
                self.one_based = False

        # Convert 1-based to 0-based if necessary
        if self.one_based:
            start = start - 1

        # Update last end position
        self._last_end = start + length

        return (column_name, start, length)


class FixedWidthRowParser:
    """
    Parses rows from a fixed-width file based on a schema.
    """

    def __init__(self, schema_file):
        """
        Initialize the parser with a schema file.

        Args:
            schema_file: File-like object containing the schema CSV
        """
        reader = csv.reader(schema_file)
        header = next(reader)
        decoder = SchemaDecoder(header)

        self.headers = []
        self.columns = []  # List of (start, end) tuples

        for row in reader:
            column_name, start, length = decoder(row)
            self.headers.append(column_name)
            self.columns.append((start, start + length))

    def parse(self, line):
        """
        Parse a fixed-width line into a list of values.

        Args:
            line: A string representing one row of fixed-width data

        Returns:
            List of stripped values
        """
        result = []
        for start, end in self.columns:
            if start < len(line):
                value = line[start:end].strip()
            else:
                value = ''
            result.append(value)
        return result
