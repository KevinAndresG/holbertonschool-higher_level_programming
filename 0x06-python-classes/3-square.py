#!/usr/bin/python3
"""a class to square of a number"""


class Square:
    """calculate the square of a number"""

    def area(self):
        """take the square of a nimber"""
        return self.__size ** 2

    def __init__(self, size=0):
        """Square class"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
