#!/usr/bin/python3
'''Class to Rectangle'''


class Rectangle:
    '''This class is create a rectangle'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Inicialization of width and height'''
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''getter to retrieve the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter to get the size'''
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        '''getter to retrieve the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter to get the size'''
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """take the square of a nimber"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__width and self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        rectangle = []
        if self.__height == 0 or self.__width == 0:
            return rectangle
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            if j != self.__width and i != self.__height:
                if (i+1) != self.__height:
                    rectangle.append('\n')
        return ("".join(rectangle))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
