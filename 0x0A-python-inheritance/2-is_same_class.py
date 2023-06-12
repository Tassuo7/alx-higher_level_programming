#!/usr/bin/python3
"""check if the object is an instance of the specified class"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance
    otherwise False"""

    if type(obj) is a_class:
        return True
    else:
        return False
