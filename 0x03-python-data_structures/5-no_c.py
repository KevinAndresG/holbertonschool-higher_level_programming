#!/usr/bin/python3
def no_c(my_string):
    run = 0
    while run < len(my_string):
        run += 1
        f = my_string.translate({ord(c): None for c in "cC"})
        return f
