#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not(roman_string):
        return 0
    rmn = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    num = 0
    for i in roman_string:
        if rmn[roman_string[i]] < rmn[roman_string[i]]:
            num -= rmn[roman_string[i]]
        else:
            num += rmn[roman_string[i]]
    return num
