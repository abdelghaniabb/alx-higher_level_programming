#!/usr/bin/python3
"""dictionary description"""


def class_to_json(obj):
    """dictionary description"""
    obj_dict = obj.__dict__

    json_dict = {}

    for key, value in obj_dict.items():
        if isinstance(value,(int, bool, str, list, dict)):
            json_dict[key] = value

    return json_dict
