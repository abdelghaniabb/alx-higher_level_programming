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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns JSON string representation of a list of dictionaries.
            Args:
                list_dictionaries: A list of dictionaries
            Returns:
                str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON string representation of list_objs to a file
            Args:
                list_objs: a list of instances that inherit from base
            Returns:
                None
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as outfile:
            for obj in list_objs:
                outfile.write(cls.to_json_string(obj.to_dictionary()))

    @staticmethod
    def from_json_string(json_string):
        """
            returns list of the JSON string representation json_string
            Args:
                json_string: a string representing a list of dictionaries
            Returns:
                list of the JSON string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
