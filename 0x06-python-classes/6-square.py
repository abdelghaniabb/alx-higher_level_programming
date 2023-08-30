#!/usr/bin/python3
"""6-square.py"""


class Square:
    """
        This class defines a square and includes methods to
        get and set its size, calculate its area and print it.
        Attributes:
            __size (int): The size of the square (private attribute).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.
        Args:
            size (int): The size of the square.
        Returns:
            None
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
            Getter method to retrieve the position of the square
            Returns:
                tuple: the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            Setter method to set the position of the square
            Args:
                value (int): The position of the square.
            Raises:
                TypeError: position must be a tuple of 2 positive integers
            Returns:
                None
        """
        if not isinstance(value, (int, int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
            Calculates and returns the area of the square.
            Returns:
                int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
            prints the square with the character #
            Returns:
                None
        """
        if self.__size == 0:
            print("")
        else:
            y = 0
            while y < self.__position[1]:
                print("")
                y = y + 1
            i = 0
            while i < self.__size:
                x = 0
                while x < self.__position[0]:
                    print(" ", end="")
                    x = x + 1
                j = 0
                while j < self.__size:
                    print("#", end="")
                    j = j + 1
                print("")
                i = i + 1
