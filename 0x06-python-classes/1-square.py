#!/usr/bin/python3
"""1-square.py"""


class Square:
    """
    This class defines a square by its size.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        self.__size = size
