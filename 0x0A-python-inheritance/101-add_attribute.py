#!/usr/bin/python3
"""adds a new attribute to an object if it’s possible"""


def add_attribute(obj, name, value):
    """if the object can’t have new attribute
    Raise a TypeError exception"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
