#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastn = number % -10
else:
    lastn = number % 10
if lastn > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastn))
elif lastn < 6 and lastn != 0:
    print("Last digit of {:d} is{:d} and is less than 6 and not 0"
          .format(number, lastn))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
