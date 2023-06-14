#!/usr/bin/python3
"""representing the Pascal’s triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers"""
    if n <= 0:
        return []

    patr = [[1]]
    while len(patr) != n:
        tr = patr[-1]
        bfr = [1]
        for i in range(len(tr) - 1):
            bfr.append(tr[i] + tr[i + 1])
        bfr.append(1)
        patr.append(bfr)
    return patr
