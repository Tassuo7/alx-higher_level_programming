#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dic = list(sorted(a_dictionary.keys()))
    for i in sort_dic:
        print("{}: {}".format(i, a_dictionary[i]))
