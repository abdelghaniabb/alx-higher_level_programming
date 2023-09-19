#!/usr/bin/python3
"""base.py"""


import json


class Base():
    """
        This class will be the “base” of all other classes in this project.
        Attributes:
            __nb_objects (int): A private class attribute to keep track
                                of the number of instances created.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize a new instance of Base
            Args:
                id: the ID to assign to the instance
            Returns:
                None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
