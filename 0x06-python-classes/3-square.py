#!/usr/bin/python3
"""3-square.py"""


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
        Returns:
            Arae of a square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
