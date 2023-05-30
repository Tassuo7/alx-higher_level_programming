#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as x:
        print("Exception: {}".format(x), file=sys.stderr)
        return None
