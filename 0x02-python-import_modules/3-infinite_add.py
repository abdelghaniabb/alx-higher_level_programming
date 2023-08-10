#!/usr/bin/python3
import sys
s = 0
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        s = s + int(sys.argv[i])
print("{}".format(s)) 
