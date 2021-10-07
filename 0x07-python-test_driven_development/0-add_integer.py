#!/usr/bin/python3
"""
function to add add two integers
a must be an integer
b must be an integer
"""


def add_integer(a, b=98):
    """
    check if a and b are intgers
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
