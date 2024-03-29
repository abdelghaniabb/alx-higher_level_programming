#!/usr/bin/python3
"""Rectangle"""


from models.base import Base


class Rectangle(Base):
    """
        defines a rectangle
        Attributes:
            __width: the width of the rectangle
            __height: the height of the rectangle
            __x: the horizontal position of the rectangle
            __y: the vertical position of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            initializes a Rectangle instance
            Args:
                width: the width of the rectangle
                height: the height of the rectangle
                x: the horizontal position of the rectangle
                y: the vertical position of the rectangle
                id: the ID of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        a, b, c = self.id, self.__x, self.__y
        e, f = self.__width, self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, e, f)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        lenght = len(args)
        if lenght == 0:
            for key, val in kwargs.items():
                setattr(self, key, val)
        elif lenght == 1:
            self.id = args[0]
        elif lenght == 2:
            self.id = args[0]
            self.__width = args[1]
        elif lenght == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        elif lenght == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        elif lenght == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
