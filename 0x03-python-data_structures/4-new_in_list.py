#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listsize = len(my_list)
    if idx >= listsize:
        return my_list[:]
    if idx < 0:
        return my_list[:]
    else:
        my_list2 = my_list.copy()
        my_list2[idx] = element
        return(my_list2)
