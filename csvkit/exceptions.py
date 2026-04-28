#!/usr/bin/env python

"""
Custom exceptions for csvkit.
"""


class CustomException(Exception):
    """
    A base exception that stores additional arguments.
    """

    def __init__(self, msg, *args):
        self.msg = msg
        self.args = args

    def __str__(self):
        if self.args:
            return self.msg % self.args
        return self.msg


class ColumnIdentifierError(CustomException):
    """
    Exception raised when invalid columns are passed.
    """
    pass


class RequiredHeaderError(CustomException):
    """
    Exception raised when the --no-header-row option is used
    but a header row is required for the operation.
    """
    pass


class InvalidValueForTypeException(CustomException):
    """
    Exception raised when a value can not be normalized to a specified type.
    """
    pass
