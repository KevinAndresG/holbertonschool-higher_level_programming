#!/usr/bin/python3
"""
displays the value of the
variable X-Request-Id
"""
if __name__ == "__main__":
    from sys import argv
    import requests
    response = requests.get(argv[1])
    print(response.headers["X-Request-Id"])
