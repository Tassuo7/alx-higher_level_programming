#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for col in line:
            if col != line[-1]:
                print("{:d}".format(col), end=" ")
            else:
                print("{:d}".format(col), end="")
        print()
