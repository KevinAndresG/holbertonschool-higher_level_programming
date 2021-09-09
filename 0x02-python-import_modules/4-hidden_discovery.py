#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    import sys
    sys.path.append('./')
    for k in dir(hidden_4):
        if k[0] != "_":
            print("{}".format(k))
