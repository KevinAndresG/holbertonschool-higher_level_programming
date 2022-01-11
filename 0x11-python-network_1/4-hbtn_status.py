#!/usr/bin/python3
""" Write a Python script that fetches """
if __name__ == "__main__":
    import requests
    response = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(str(response))))
    print("\t- content: {}".format(response.text))
