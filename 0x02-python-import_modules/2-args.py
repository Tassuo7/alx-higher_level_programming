#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    i = 1
    if len(argv) == 0:
        print("0 arguments.")
    elif len(argv) == 1:
        print("1 argument:\n1: {}".format(argv))
    else:
        print("{} arguments:".format(len(argv)))
        for i in range(len(argv)):
            print("{}: {}".format(i, argv[i]))
