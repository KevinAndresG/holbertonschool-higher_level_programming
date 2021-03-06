#!/usr/bin/python3
"""Square class"""


class Square:
    """Square"""
    pass

    def __init__(self, size=0):
        """Square class"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
