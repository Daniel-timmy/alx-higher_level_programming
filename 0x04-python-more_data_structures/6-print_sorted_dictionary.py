#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    d_keys = list(a_dictionary.keys()).sort()

    for i in d_keys:
        print("{}: {}".format(i, a_dictionary[i]))
