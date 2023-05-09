#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n_str = repr(abs(number))
n = int(n_str[-1])
if number < 0:
    n = - n
if n > 5:
    str = "and is greater than 5"
elif n == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"
print(f"Last digit of {number} is {n} {str}")
