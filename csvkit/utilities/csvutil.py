#!/usr/bin/env python

"""
Base class for all csvkit utilities.
"""

import sys
import agate


class CSVKitUtility:
    """
    Base class for all csvkit utilities.
    """

    description = 'A csvkit utility.'

    def __init__(self, args=None, output_file=None, error_file=None):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    @classmethod
    def launch_new_instance(cls):
        raise NotImplementedError

    def add_arguments(self):
        pass

    def main(self):
        raise NotImplementedError
