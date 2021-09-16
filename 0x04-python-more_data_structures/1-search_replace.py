def search_replace(my_list, search, replace):

    k = my_list.copy()
    if search in my_list:
        for e, i in enumerate(k):
            if i == search:
            	k[e] = replace
    return k
