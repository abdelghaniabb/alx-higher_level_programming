#!/usr/bin/python3
"""student"""


class Student():
    """
        defines a student
    """
    def __init__(self, first_name="", last_name="", age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            # If attrs is None, retrieve all attributes
            return self.__dict__
        else:
            # Create an empty dictionary to store selected attributes
            result = {}
            for attr_name in attrs:
                if hasattr(self, attr_name):
                    # Check if the attribute exists in the object
                    result[attr_name] = getattr(self, attr_name)
            return result
