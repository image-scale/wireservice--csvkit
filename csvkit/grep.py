#!/usr/bin/env python

"""
Filtering CSV reader that supports pattern matching.
"""

import re

from csvkit.exceptions import ColumnIdentifierError


class FilteringCSVReader:
    """
    A CSV reader that filters rows based on patterns.
    """

    def __init__(self, reader, patterns=None, header=True, inverse=False, any_match=False):
        """
        Initialize the filtering reader.

        Args:
            reader: An iterable of rows (lists of values)
            patterns: Either a list of patterns (applied to any column) or a dict
                     mapping column indices/names to patterns. Patterns can be
                     strings or compiled regex objects.
            header: If True, the first row is a header and is always returned
            inverse: If True, return rows that do NOT match
            any_match: If True, return rows where ANY pattern matches (OR logic).
                      If False, return rows where ALL patterns match (AND logic).
        """
        self.reader = iter(reader)
        self.header = header
        self.inverse = inverse
        self.any_match = any_match
        self.header_row = None
        self.returned_header = False

        # Process patterns
        if patterns is None:
            self.patterns = {}
        elif isinstance(patterns, dict):
            self.patterns = patterns
        else:
            # List of patterns - apply to all columns
            self.patterns = patterns

        # If we have a header and dict patterns, read header now to validate
        if self.header and isinstance(self.patterns, dict) and self.patterns:
            self.header_row = next(self.reader)
            self._normalize_patterns()

    def __iter__(self):
        return self

    def __next__(self):
        # If we need to return the header first
        if self.header and not self.returned_header:
            self.returned_header = True
            if self.header_row is None:
                self.header_row = next(self.reader)
                # Validate patterns - check for duplicate column identifiers
                if isinstance(self.patterns, dict):
                    self._normalize_patterns()
            return self.header_row

        # Filter rows
        while True:
            row = next(self.reader)

            if self._matches(row):
                return row

    def _normalize_patterns(self):
        """
        Convert column names in patterns to indices and check for duplicates.
        """
        normalized = {}
        for key, pattern in self.patterns.items():
            if isinstance(key, str):
                # Convert column name to index
                try:
                    idx = self.header_row.index(key)
                except ValueError:
                    raise ColumnIdentifierError("Column '%s' not found in header.", key)
            else:
                idx = key

            if idx in normalized:
                raise ColumnIdentifierError(
                    "Duplicate column identifier: '%s' and '%s' both refer to column %d.",
                    key, idx, idx
                )

            normalized[idx] = pattern

        self.patterns = normalized

    def _matches(self, row):
        """
        Check if a row matches the patterns.
        """
        if isinstance(self.patterns, list):
            # Patterns apply to any column
            matches = self._match_any_column(row)
        else:
            # Patterns are dict of column -> pattern
            if self.any_match:
                matches = any(
                    self._match_value(self._get_value(row, idx), pattern)
                    for idx, pattern in self.patterns.items()
                )
            else:
                matches = all(
                    self._match_value(self._get_value(row, idx), pattern)
                    for idx, pattern in self.patterns.items()
                )

        if self.inverse:
            return not matches
        return matches

    def _match_any_column(self, row):
        """
        Check if any column in the row matches any pattern in the list.
        """
        for pattern in self.patterns:
            for value in row:
                if self._match_value(value, pattern):
                    return True
        return False

    def _get_value(self, row, idx):
        """
        Get a value from a row by index, handling out-of-range gracefully.
        """
        if idx < len(row):
            return row[idx]
        return ''

    def _match_value(self, value, pattern):
        """
        Check if a value matches a pattern.

        Pattern can be a string (substring match) or a compiled regex.
        """
        if hasattr(pattern, 'search'):
            # It's a regex
            return pattern.search(value) is not None
        else:
            # String match
            return pattern in value
