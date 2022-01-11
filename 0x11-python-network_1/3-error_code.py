#!/usr/bin/python3
"""  """
import urllib.request
from sys import argv

req = urllib.request.Request(argv[1])
try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
