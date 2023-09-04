#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
displays the body of the response
"""
import sys
import requests as req


if __name__ == "__main__":
    url = sys.argv[1]
    eml = {'email': sys.argv[2]}
    print(req.post(url, eml).text)
