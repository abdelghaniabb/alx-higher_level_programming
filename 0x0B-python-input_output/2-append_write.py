#!/usr/bin/python3
"""append a string at the end of a file"""


def append_write(filename="", text=""):
    """
        appends a string at the end of a file
            Args:
                filename: the name of the file
            text: the text to add to the file
        Returns:
            number of char that added to the fole
    """
    with open(filename, "a", encoding="utf-8") as outfile:
        count = 0
        for char in text:
            outfile.write(char)
            count += 1
        return count
