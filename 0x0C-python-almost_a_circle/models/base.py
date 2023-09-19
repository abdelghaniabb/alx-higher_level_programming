#!/usr/bin/python3
"""base.py"""


import json
import csv


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
        filename = "{}.json".format(cls.__name__)
        obj_list = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w") as file:
            file.write(cls.to_json_string(obj_list))

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            Serialize and save a list of instances to a CSV file.
            Args:
                cls: The class type.
                list_objs: A list of instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline='') as outfile:
            writer = csv.writer(outfile)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
            Deserialize and load instances from a CSV file.
            Args:
                cls: The class type.
            Returns:
                A list of instances.
        """
        filename = cls.__name__ + ".csv"
        instance_list = []
        try:
            with open(filename, mode="r", newline='') as infile:
                reader = csv.reader(infile)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    instance_list.append(instance)
            return instance_list
        except FileNotFoundError:
            return []
