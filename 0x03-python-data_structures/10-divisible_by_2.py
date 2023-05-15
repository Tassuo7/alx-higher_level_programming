#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lr = []
    for n in my_list:
        if (n % 2) == 0:
            lr.append(True)
        else:
            lr.append(False)
    return lr
