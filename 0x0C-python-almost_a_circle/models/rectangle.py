#!/usr/bin/python3
"""

"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''getter to retrieve the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter to get the size'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''getter to retrieve the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter to get the size'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        '''getter to retrieve the width'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter to get the size'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''getter to retrieve the width'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter to get the size'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__y = value
