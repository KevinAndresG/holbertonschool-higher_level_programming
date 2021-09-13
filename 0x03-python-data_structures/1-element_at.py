#!/usr/bin/python3
def element_at(my_list, idx):
    listsize = len(my_list)
    sizze = 0
    if idx > listsize:
        return None
    if idx < 0:
        return None
    else:
        while sizze < idx:
            sizze += 1
        return my_list[sizze]
