#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = list_length
    len1 = len(my_list_1)
    len2 = len(my_list_2)
    i = 0

    try:
        if len1 != len2:
            print("out of range")
        else:
            for i in my_list_1, my_list_2:
                return my_list_1[i] / my_list_2[i]
    except TypeError:
        print("division by 0")
        return length
