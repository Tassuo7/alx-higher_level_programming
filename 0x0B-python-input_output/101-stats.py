#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys


def print_stats(size, status_code):
    """Print accumulated metrics."""
    print("File size: {}".format(size))
    for k in sorted(status_code):
        print("{}: {}".format(k, status_code[k]))

size = 0
status_code = {}
poss_code = ['200', '301', '400', '401', '403', '404', '405', '500']
numb = 0

try:
    for line in sys.stdin:
        if numb == 10:
            print_stats(size, status_code)
            numb = 1
        else:
            numb += 1
        line = line.split()
        try:
            size += int(line[-1])
        except (IndexError, ValueError):
            pass
        try:
            if line[-2] in poss_code:
                if status_code.get(line[-2], -1) == -1:
                    status_code[line[-2]] = 1
                else:
                    status_code[line[-2]] += 1
        except IndexError:
            pass
    print_stats(size, status_code)
except KeyboardInterrupt:
    print_stats(size, status_code)
    raise
