#!/usr/bin/python3
""" script that takes in a URL and an email """
if __name__ == "__main__":
   import urllib.parse
   import urllib.request
   from sys import argv

   url = argv[1]
   values = {"mail": argv[2]}

   data = urllib.parse.urlencode(values)
   data = data.encode("ascii")  # turn data in bytes
   req = urllib.request.Request(url, data)
   with urllib.request.urlopen(req) as response:
      print(response.decode("utf8"))
