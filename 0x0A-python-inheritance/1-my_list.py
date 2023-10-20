#!/usr/bin/python3
"""1-my_list.py"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """
            prints the list in ascending sort
        """
        print(sorted(self))
