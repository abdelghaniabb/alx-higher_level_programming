#!/usr/bin/python3
""" Say my name"""


def say_my_name(first_name, last_name=""):
    """
        prints my name
        Args:
            first_name:string
            last_name: string
        Raises:
            TypeError: the args must be strings
            Returns:
                None
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
