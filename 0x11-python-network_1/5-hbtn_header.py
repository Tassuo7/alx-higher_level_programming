#!/usr/bin/python3
"""
sends a request to the URL
idisplays the value of the variable X-Request-Id
"""
import sys
import requests as r


if __name__ == "__main__":
    url = sys.argv[1]
    print(r.get(url).headers.get("X-Request-Id"))
