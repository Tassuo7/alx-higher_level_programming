#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    add_list = set(my_list)
    for i in add_list:
        add += i
    return add
