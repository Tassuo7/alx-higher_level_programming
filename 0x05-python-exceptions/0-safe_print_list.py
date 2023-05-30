#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    hmx = 0
    try:
        for elem in range(x):
            print("{:d}".format(my_list[elem]), end="")
            hmx += 1
    except IndexError:
        break
    print()
    return hmx
