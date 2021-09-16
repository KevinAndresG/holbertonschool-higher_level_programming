def search_replace(my_list, search, replace):
    l = int(search)
    l2 = int(replace)
    k = my_list.copy()
    if search >= len(my_list):
        return my_list
    if search < 0:
        return my_list
    else:
        for e, i in enumerate(my_list):
            if i == l:
                k[e] = replace

    return k
