#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    i = 0
    if n < 0:
        n = len(str) + n
    for c in str:
        if i != n:
            s = s + c
        i = i + 1
    return s

    
