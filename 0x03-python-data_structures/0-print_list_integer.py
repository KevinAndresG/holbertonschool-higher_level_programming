#!/usr/bin/python3
def print_list_integer(my_list=[]):
    count = 0
    count2 = len(my_list)
    while count < count2:
        print('{}'.format(my_list[count]))
        count += 1
