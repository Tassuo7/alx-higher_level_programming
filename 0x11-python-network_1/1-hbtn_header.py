#!/usr/bin/python3
"""
send a request to the URL and displays the value of the X-Request-Id
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        print(res.info().get('X-Request-Id'))
