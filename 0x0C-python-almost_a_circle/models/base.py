#!/usr/bin/python3
"""Base"""


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

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    """def save_to_file(cls, list_objs):
        writes the JSON string representation of list_objs to a file
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf-8") as outfile:
            outfile.write(cls.to_json_string(json_list))
    """
