#!/usr/bin/python3
""" Python script that takes in a URL """
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv

    with request.urlopen(argv[1]) as response:
    	print(response.headers["X-Request-Id"])
