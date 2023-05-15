#!/usr/bin/python3
def check(tuple_=(), i):
    if len(tuple_) >= i + 1:
        a = tuple_[i]
    else:
        a = 0
    return a
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = check(tuple_a, 0)
    a2 = check(tuple_a, 1)
    b1 = check(tuple_b, 0)
    b2 = check(tuple_b, 1)
    return (a1 + b1, a2 + b2)
print(add_tuple((1, 2), (1,2)))    