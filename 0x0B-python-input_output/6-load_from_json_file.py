#!/usr/bin/python3
"""
open a json file and
convert in a
python object
"""
import json


def load_from_json_file(filename):
    """
    object
    """
    with open(filename, 'r') as file:
        return json.load(file)
