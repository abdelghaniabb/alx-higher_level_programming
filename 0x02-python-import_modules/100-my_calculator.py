#!/usr/bin/python3
import sys
import calcumator_1 as c

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    n1 = int(sys.argv[1])
    op = sys.argv[2]
    n2 = int(sys.argv[3])
    if op == '+':
        print("{:d} {:s} {:d} = {:d}".format(n1, op, n2, c.add(n1, n2)))
    elif op == '-':
        print("{:d} {:s} {:d} = {:d}".format(n1, op, n2, c.sub(n1, n2)))
    elif op == '*':
        print("{:d} {:s} {:d} = {:d}".format(n1, op, n2, c.mul(n1, n2)))
    elif op == '/':
        print("{:d} {:s} {:d} = {:d}".format(n1, op, n2, c.div(n1, n2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
