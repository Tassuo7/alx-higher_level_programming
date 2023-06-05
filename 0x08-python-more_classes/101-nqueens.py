#!/usr/bin/python3
"""a program that solves the N queens problem"""


import sys
N = sys.argv[1]
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if N.isdigit() is False:
    print("N must be a number")
    exit(1)
if int(N) < 4:
    print("N must be at least 4")
    exit(1)
