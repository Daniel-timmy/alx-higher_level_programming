#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        l_digit = number % 10
    else:
        number = number * -1
        l_digit = number % 10
    print("{:d}".format(l_digit), end='')
    return (l_digit)
