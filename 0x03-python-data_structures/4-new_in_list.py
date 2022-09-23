#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        new_l = my_list[:]
        return (new_l)
    if idx >= len(my_list):
        new_l = my_list[:]
        return (new_l)
    new_l = my_list[:]

    new_l[idx] = element

    return (new_l)
