#!/usr/bin/python3
""" a class LockedClass with no class or object attribute """


class LockedClass:
    """ prevents user from dynamically creating new instance
    except if the new instance attribute is called first_name"""
    __slots__ = ['first_name']
