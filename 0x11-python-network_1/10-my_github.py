#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
uses the GitHub API to display your id.
"""
import requests as req
import sys


if __name__ == "__main__":
    auth = (sys.argv[1], sys.argv[2])
    url = "https://api.github.com/user"
    disp = req.get(url, auth=auth)
    print(disp.json().get("id"))
