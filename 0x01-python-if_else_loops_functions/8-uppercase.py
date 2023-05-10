#!/usr/bin/python3
def uppercase(str):
    ns = ""
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            ns = ns + chr(ord(c) - 32)
            #print("{}".format(chr(ord(c) - 32)), end="")
        else:
            ns = ns + c
            #print("{}".format(c), end="")
    print("{}".format(ns))
