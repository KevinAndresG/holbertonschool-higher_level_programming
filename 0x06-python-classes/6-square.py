#!/usr/bin/python3
"""calculate the square of a number"""


class Square:
    """calculate the square of a number"""

    def __init__(self, size=0, position=(0, 0)):
        """Square class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter func"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter func"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) and type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """take the square of a nimber"""
        return self.__size ** 2

    def my_print(self):
        '''This method print a squere in #'''
        self.square = self.__size
        if self.square == 0:
            print()
            return
        for i in range(self.square):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(self.__position[1]):
                if self.__position[1] > 0:
                    print("", end="")
                # else:
                #     print(" ", end="")
            for i in range(self.square):
                print("#", end="")
            print()
