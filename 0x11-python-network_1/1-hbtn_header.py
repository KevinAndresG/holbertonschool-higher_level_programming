#!/usr/bin/python3
""" Python script that takes in a URL """
import urllib.request as request
from sys import argv
response = request.urlopen(argv[1])
print(response.headers['X-Request-Id'])
