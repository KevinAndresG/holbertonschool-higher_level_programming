#!/usr/bin/python3
"""
check
the class
and sub class
"""


def inherits_from(obj, a_class):
    """
    comparing
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
