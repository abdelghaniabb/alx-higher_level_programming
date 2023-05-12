#!/usr/bin/python3
import sys
if __name__ != "__main__":
    exit()
argv = sys.argv
argc = len(argv) - 1
sum = 0
for i in range(1, argc + 1):
    sum = sum + int(argv[i])
print(sum)
