#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv)
    count = 1
    if size == 1:
        print('0 arguments.')
    else:
        print('{} arguments:'.format(size - 1))
    while count < size:
        print('{}: {}'.format(count, sys.argv[count]))
        count = count + 1
