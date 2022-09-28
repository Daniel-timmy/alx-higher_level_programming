#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_n = set(my_list)

    sum_n = 0
    for i in list_n:
        sum_n += i

    return (sum_n)
