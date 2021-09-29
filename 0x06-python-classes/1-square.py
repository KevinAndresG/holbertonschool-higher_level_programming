#!/usr/bin/python3
"""Square class"""


class Square:
    __size = None
"""size of square"""


def __init__(self, size=None):
    self.__size = size
    print("_Square__size:{}".format(size))
