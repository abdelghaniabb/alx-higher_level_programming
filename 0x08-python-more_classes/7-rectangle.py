#!/usr/bin/python3
"""1-rectangle.py"""


class Rectangle:
    """
        this defines a rectangle
        Attributes:
            width:
            height:
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Initializes a new rectangle
            Args:
                width
                height
            Returns:
                None
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            Getter method to retrieve the width of the rectangle
            Returns:
                width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter method to set the width of the rectangle
            Args:
                value
            Raises:
                TypeError: width must be an integer
                ValueError: width must be >= 0
            Returns:
                None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Getter method to get the height
            Returns:
                height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter method to set the height
            Args:
                value
            Raises:
                TypeError: height must be an integer
                ValueError: height must be >= 0
            Returns:
                None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = str(self.print_symbol) * self.__width + "\n"
        return rectangle_str * (self.__height - 1) + str(self.print_symbol) * self.__width

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
