#!/usr/bin/python3
"""square.py"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        defines a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initializes a square instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """returns [square] (<id>) <x>/<y> - <size>"""
        a, b, c = self.id, self.x, self.y
        e = self.width
        return "[Square] ({}) {}/{} - {}".format(a, b, c, e)

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
            self.size = args[1]
        elif lenght == 3:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
        elif lenght == 4:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
