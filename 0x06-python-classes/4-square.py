#!/usr/bin/python3
"""4-square.py"""


class Square:
    """
        This class defines a square and includes methods to
        get and set its size and calculate its area.
        Attributes:
            __size (int): The size of the square (private attribute).
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.
        Args:
            size (int): The size of the square.
        Returns:
            None
        """

        self.__size = size

    @property
    def size(self):
        """
            Getter method to retrieve the size of the square
            Returns:
                int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Setter method to set the size of the square
            Args:
                value (int): The size of the square.
            Raises:
                TypeError: size is not integer
                ValueError: Size < 0
            Returns:
                None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
            Calculates and returns the area of the square.
            Returns:
                int: The area of the square.
        """
        return self.__size ** 2
