#!/usr/bin/python3
"""function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """using a JSON representation writes an Object"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
