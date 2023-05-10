#!/usr/bin/python3
def pow(a, b):
    p = 1
    if b == 0:
        return p
    if b < 0:
        for i in range(1, abs(b) + 1):
            p = p * 1 / a
        return p
    for i in range(1, b + 1):
        p = p * a    
    return p

