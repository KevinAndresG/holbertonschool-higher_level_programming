#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    sum = my_list[1]
    size = len(my_list)
    for i in range(0, size - 1):
        if (my_list[i] != my_list[i+1]):
            sum = sum + my_list[i+1]
    return sum
