#!/usr/bin/python3
"""function that returns an object"""
import json


def from_json_string(my_str):
    """represente Python data structure by a JSON string"""
    return json.loads(my_str)
