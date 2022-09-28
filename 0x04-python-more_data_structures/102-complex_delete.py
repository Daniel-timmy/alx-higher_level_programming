#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_n = a_dictionary.keys()

    for i in keys_n:
        if value == a_dictionary.get(i):
            pop_n = a_dictionary.pop(i)
    return (a_dictionary)
