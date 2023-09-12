#!/usr/bin/python3
"""read a text file"""


def read_file(filename=""):
    """read a text file and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as infile:
        print(infile.read(), end="")
