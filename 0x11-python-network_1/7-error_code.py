#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
"""
import sys
import requests as req


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        print(req.get(url).raise_for_status().text)
    except req.exceptions.HTTPError as err:
        print(f"Error code: {err.response.status_code}")
