#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    k = lambda key: value if key in a_dictionary else a_dictionary[key] = value
    # if key in a_dictionary:
    #     a_dictionary[key] = value
    # a_dictionary[key] = value
    return k
