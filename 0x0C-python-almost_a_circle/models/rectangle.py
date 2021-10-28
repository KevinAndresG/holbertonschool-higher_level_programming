#!/usr/bin/python3
"""
here just going to create
the getter and setter
to moodify it
"""
from models.base import Base
"""
import the super class
"""


class Rectangle(Base):
    """
    a clas to make a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

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
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''getter to retrieve the x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter to get the size'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''getter to retrieve the y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter to get the size'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area"""
        return self.__width * self.__height

    def display(self):
        """display a rectangle"""
        print("\n" * self.y, end="")

        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for k in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ void str """
        return(f"[Rectangle] \
({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")
