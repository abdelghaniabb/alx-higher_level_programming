#!/usr/bin/python3

"""2-square.py"""


class Square:
    """
        This class defines a square by its size.
        Attributes:
            __size (int): The size of the square (private attribute).
    """
    def __init__(self, size=0):
        """Constructor
            Args:
                size: The size of the square.
            Raises:
                    TypeError: size is not integer
                    ValueError: Size < 0
        """
        if not(type(size) == int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
