#!/usr/bin/python3
"""
print a sorted
list from a class
previously added
"""


class MyList(list):
    def print_sorted(self):
        """
        sort the list
        """
        print(sorted(self))
