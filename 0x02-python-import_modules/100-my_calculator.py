#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    c = argv[2]
    if argv[2] == '+':
        print("{} {} {} = {}".format(a, c, b, add(a, b)))
    elif argv[2] == '-':
        print("{} {} {} = {}".format(a, c, b, sub(a, b)))
    elif argv[2] == '*':
        print("{} {} {} = {}".format(a, c, b, mul(a, b)))
    elif argv[2] == '/':
        print("{} {} {} = {}".format(a, c, b, div(a, b)))
