#!/usr/bin/python3
"""
lists 10 commits of a repository using the GitHub API.
"""
import requests as r
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    own = sys.argv[2]
    url = f"https://api.github.com/repos/{own}/{repo}/commits"
    try:
        rgets = r.get(url)
        rgets.raise_for_status()
        comts = rgets.json()[:10]
        for i in comts:
            sha = i.get('sha')
            auth = i.get('commit').get('author').get('name')
            print(f"{sha}: {auth}")
    except r.exceptions.RequestException as x:
        print(f"Error: {x}")
        sys.exit(1)
