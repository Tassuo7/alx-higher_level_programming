#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for item in matrix:
        new_matrix = list(map(lambda x: x**2, item))
    return new_matrix
