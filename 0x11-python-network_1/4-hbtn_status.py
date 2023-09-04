#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
import requests as req


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    print("Body response:")
    print("\t- type: {}".format(type(req.get(url).text)))
    print("\t- content: {}".format(req.get(url).text))
