#!/usr/bin/python3
"""
sends a request to the URL
displays the body of the response (decoded in utf-8)
"""
import sys
from urllib import request, error


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
