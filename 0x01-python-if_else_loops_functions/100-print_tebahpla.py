#!/usr/bin/python3
for alt in range(122, 96, -1):
    if alt % 2 == 0:
        j = alt
    else:
        j = alt - 32
    print("{:c}".format(j), end="")
