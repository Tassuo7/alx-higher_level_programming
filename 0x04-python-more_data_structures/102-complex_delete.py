#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    kys = list(a_dictionary.keys())
    for k in kys:
        if a_dictionary[k] == value:
            del a_dictionary[k]
    return a_dictionary
