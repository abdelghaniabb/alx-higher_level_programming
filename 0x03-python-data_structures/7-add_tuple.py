#!/usr/bin/python3
def check(i, tuple_=None):
    if tuple_ is None or len(tuple_) < i + 1:
        a = 0
    else:
        a = tuple_[i]
    return a
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or len(tuple_a) < 1:
        a1 = 0
    else:
        a1 = tuple_a[0]
    if tuple_a is None or len(tuple_a) < 2:
        a2 = 0
    else:
        a2 = tuple_a[1]
    if tuple_b is None or len(tuple_b) < 1:
        b1 = 0
    else:
        b1 = tuple_b[0]
    if tuple_b is None or len(tuple_b) < 2:
        b2 = 0
    else:
        b2 = tuple_b[1]
    return (a1 + b1, a2 + b2)
