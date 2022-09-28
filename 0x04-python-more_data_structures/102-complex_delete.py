#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_n = a_dictionary.keys()

    for i in keys_n:
        if value == a_dictionary.get(i):
            a_dictionary.pop(i)
        else:
            pass
    return (a_dictionary)
