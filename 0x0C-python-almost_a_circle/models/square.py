#!/usr/bin/python3
"""
import the Rectangle
class to make the
Square class
"""
from models.rectangle import Rectangle
"""
importing the class to inherit
"""


class Square(Rectangle):
    """
        a class to print a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initializate the args"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ print the sintaxis """
        return(f"[Square] \
({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """to retrieve it"""
        return self.width

    @size.setter
    def size(self, value):
        """to set it"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
