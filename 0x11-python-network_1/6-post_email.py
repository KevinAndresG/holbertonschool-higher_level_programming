#!/usr/bin/python3
"""
POST request to the passed URL
with the email as a parameter
"""
if __name__ == "__main__":
    from sys import argv
    import requests
    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
