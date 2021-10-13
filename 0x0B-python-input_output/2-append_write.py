#!/usr/bin/python3
"""
open
and write toat end
"""


def append_write(filename="", text=""):
    """
    open the file
    """
    with open(filename, 'a') as file:
        return file.write(text)
