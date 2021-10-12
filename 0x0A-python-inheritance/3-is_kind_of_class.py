#!/usr/bin/python3
"""
compare
two clases
and return it
"""


def is_kind_of_class(obj, a_class):
    """
    compare with isinstance
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
