#!/usr/bin/python3
"""
function to print the name
the first name must be a string
the last name must be a string
"""


def say_my_name(first_name, last_name=""):
    """
    if the first name or lasdt name is != str raise an error
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print('My name is {} {}'.format(first_name, last_name))
