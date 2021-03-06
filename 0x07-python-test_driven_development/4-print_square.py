#!/usr/bin/python3
"""
print a square of #
size is the size of the square.
a jump of line after each square
"""


def print_square(size):
    """
    size must be a integer number
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(type(size), int) is False and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print("")
