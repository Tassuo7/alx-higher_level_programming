#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    scr = 0
    wght = 0
    for i in my_list:
        scr += i[0] * i[1]
        wght += i[1]
    return (scr/wght)
