#!/usr/bin/python3
"""a program that solves the N queens problem"""


import sys
if len(sys.args) != 2:
    print("Usage: nqueens N")
    exit(1)
N = sys.args[1]
if type(N) is not int:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)
