#!/usr/bin/python3
"""write a string to a text file"""


def write_file(filename="", text=""):
    """
        writes a string to a text file
        Args:
            filename: the name of the file
            text: the text to add to the file
        Returns:
            number of char that added to the fole
    """
    with open(filename, "w", encoding="utf-8") as outfile:
        i = 0
        for char in text:
            outfile.write(char)
            i += 1
        return i
