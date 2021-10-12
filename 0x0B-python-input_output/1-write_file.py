#!/usr/bin/python3
"""
open a file
and return
the files writen
"""


def write_file(filename="", text=""):
    """
    hi
    """
    """if not filename:"""
    with open(filename, 'w') as f:
    	return f.write(text)
