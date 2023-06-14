#!/usr/bin/python3
"""script that adds all arguments to a Python list"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    arglis = load_from_json_file("add_item.json")
except Exception:
    arglis = []
arglis += sys.argv[1:]
save_to_json_file(arglis, "add_item.json")
