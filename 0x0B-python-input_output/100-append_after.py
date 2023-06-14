#!/usr/bin/python3
"""function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a specific string"""
    txt = ""
    with open(filename) as r:
        for ln in r:
            txt += ln
            if search_string in ln:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
