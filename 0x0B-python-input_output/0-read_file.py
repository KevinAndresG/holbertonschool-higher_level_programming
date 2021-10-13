#!/usr/bin/python3
"""
opne and read
an text file
"""


def read_file(filename=""):
    """
    open a file and read
    """
    with open(filename) as f:
        read_data = f.read()
        print(read_data, end="")
    f.closed
