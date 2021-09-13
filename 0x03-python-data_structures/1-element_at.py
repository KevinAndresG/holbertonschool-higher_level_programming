#!/usr/bin/python3
def element_at(my_list, idx):
    listsize = len(my_list)
    sizze = idx
    if idx > listsize:
        return None
    elif idx < 0:
        return None
    else:
   	 return my_list[sizze]
