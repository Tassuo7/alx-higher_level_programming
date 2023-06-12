#!/usr/bin/python3
"""class MyInt rebel integer class"""


class MyInt(int):
    """the class MyInt that inherits frm int
    has == and != operators inverted"""
    def __eq__(self, other):
        """equal is not equal"""
        return (super().__ne__(other))

    def __ne__(self, other):
        """not equal is equal"""
        return (super().__eq__(other))
