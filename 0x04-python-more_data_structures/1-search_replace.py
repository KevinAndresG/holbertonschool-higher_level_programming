def search_replace(my_list, search, replace):
    l = int(search)
    l2 = int(replace)
    k = my_list.copy()
    for e, i in enumerate(k):
        if i == l:
            k[e] = l2
    return k
