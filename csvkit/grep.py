#!/usr/bin/env python

"""
Filtering CSV reader that supports pattern matching.
"""


class FilteringCSVReader:
    """
    A CSV reader that filters rows based on patterns.
    """

    def __init__(self, reader, patterns=None, header=True, inverse=False, any_match=False):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __next__(self):
        raise NotImplementedError
