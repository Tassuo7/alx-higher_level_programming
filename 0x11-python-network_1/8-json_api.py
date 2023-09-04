#!/usr/bin/python3
"""
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests as req
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    try:
        data = req.post(u, data={'q': q}).json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
