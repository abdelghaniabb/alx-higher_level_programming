#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n_str = repr(number)
n = int(n_str[-1])
if n > 5:
    str = "and is greater than 5"
elif n == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"
print(f"Last figit of {number} is {n_str[-1]} {str}")
