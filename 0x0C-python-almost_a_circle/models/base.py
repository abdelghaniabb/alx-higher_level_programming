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

    @classmethod
    def create(cls, **dictionary):
        """
            creates and returns an instace with all attributes
            already set based on the given dictionary
            Args:
                dictionary: A dictionary containing attribute values.
            Returns:
                an instace with all attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a JSON file and returns a list of instances.
        Returns:
            list: A list of instances loaded from the file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as infile:
                data = infile.read()
                obj_list = cls.from_json_string(data)
                return [cls.create(**obj_dict) for obj_dict in obj_list]
        except FileNotFoundError:
            return []
