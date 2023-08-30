#!/usr/bin/python3

"""2-square.py"""


class Square:
    """
    This class defines a square by its size.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
                TypeError: size is not integer
                ValueError: Size < 0
        """

        try:
            if not(type(size) == int and int(size) >= 0):
                self.__size = int("size")
            self.__size = size
        except Exception:
            if int(size) < 0:
                raise ValueError("size must be >= 0")
            raise TypeError("size must be an integer")
