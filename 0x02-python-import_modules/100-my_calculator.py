#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
argv = sys.argv
argc = len(argv)
if argc != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
if argv[2] == '+':
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], add(int(argv[1]), int(argv[3]))))
elif argv[2] == '-':
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], sub(int(argv[1]), int(argv[3]))))
elif argv[2] == '*':
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], mul(int(argv[1]), int(argv[3]))))
elif argv[2] == '/':
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], div(int(argv[1]), int(argv[3]))))

