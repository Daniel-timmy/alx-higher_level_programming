#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys_n = a_dictionary.keys()
    dict_n = {}

    for i in keys_n:
        dict_n[i] = 2 * a_dictionary.get(i)

    return (dict_n)
