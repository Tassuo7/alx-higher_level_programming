#!/usr/bin/python3
"""check if the object is an instance of, or 
an instance of a class that inherited the specified class"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance
    otherwise False"""

    return (isinstance(obj, a_class))
