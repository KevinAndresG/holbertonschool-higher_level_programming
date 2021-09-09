#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    ad = ('{}' ' + ' '{}'' = ''{}'.format(a, b, add(a, b)))
    su = ('{}' ' - ' '{}'' = ''{}'.format(a, b, sub(a, b)))
    mu = ('{}' ' * ' '{}'' = ''{}'.format(a, b, mul(a, b)))
    di = ('{}' ' / ' '{}'' = ''{}'.format(a, b, div(a, b)))
    print("{}".format(ad))
    print("{}".format(su))
    print("{}".format(mu))
    print("{}".format(di))
