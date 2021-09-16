#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == None:
        return None
    k = my_list.copy()
    if search in my_list:
        for e, i in enumerate(k):
            if i == search:
                k[e] = replace
    return k
