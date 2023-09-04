#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.parse as urlp
import urllib.request as urlr


if __name__ == "__main__":
    ur = sys.argv[1]
    eml = {"email": sys.argv[2]}
    data = urlp.urlencode(eml).encode("ascii")

    req = urlr.Request(ur, data)
    with urlr.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
