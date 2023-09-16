#!/usr/bin/python3
"""search and update"""


def append_after(filename="", search_atring="", new_string=""):
    """
         inserts a line of text to a file, after
         each line containing a specific string
    """
    with open(filename, "r", encoding="utf-8") as infile:
        text = infile.readlines()
        infile.close()

    with open(filename, "w", encoding="utf-8") as outfile:
        outfile.write(new_string)
        for line in text:
            outfile.write(line)
            if search_atring in line:
                outfile.write(new_string)
