#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    i = 1
    if argv == 0:
        print("0 arguments.")
    elif argv == 1:
        print("1 argument:\n1: {}".format(argv))
    else:
        print("{} arguments:".format(len(argv)))
        for i in range(len(argv) - 1):
            print("{}: {}".format(i, argv[i]))
