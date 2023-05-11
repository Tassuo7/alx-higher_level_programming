#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    adds = 0
    for i in range(len(argv) - 1):
        adds = adds + int(argv[i + 1])
    print("{}".format(adds))
