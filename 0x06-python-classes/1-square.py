#!/usr/bin/python3
"""Square class"""


class Square:
    __size = None

    def __init__(self, size):
        """size of a Square"""
        if Square.__size is None:
            self.__size = size
