#!/usr/bin/python3
def element_at(my_list, idx):
    listsize = len(my_list)
    if idx > listsize:
        return None
    if idx < 0:
        return None
    else:
   	 return my_list[idx]
