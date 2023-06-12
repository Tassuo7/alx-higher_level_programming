#!/usr/bin/python3
"""check if the object is an instance of a class that inherited
the specified class"""


def inherits_from(obj, a_class):
    """True if the object is an instance of the class
    otherwise False"""

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
