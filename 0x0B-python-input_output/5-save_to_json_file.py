#!/usr/bin/python3
"""
a
a
a
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a
    """
    with open(filename, 'w') as file:
        return file.write(json.dumps(my_obj))
