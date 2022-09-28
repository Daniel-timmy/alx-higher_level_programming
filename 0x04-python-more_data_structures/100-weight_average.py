#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)

    score = [list1[0] for list1 in my_list]
    weight = [list2[1] for list2 in my_list]
    sum_w = 0
    sum_s = 0
    for (a, b) in zip(score, weight):
        sum_s += (a * b)
        sum_w += b

    return (sum_s/sum_w)
