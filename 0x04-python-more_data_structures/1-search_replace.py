def search_replace(my_list, search, replace):
    l = int(search)
    l2 = int(replace)
    if search >= len(my_list):
        return my_list
    if search < 0:
        return my_list
    else:
        k = my_list.copy()
        k[l - 1] = l2
    return k
