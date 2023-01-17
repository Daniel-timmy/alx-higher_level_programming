#!/usr/bin/python3
"""takes in a URL, sends a request to the URL"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        id_x = response.headers['X-Request-Id']
        print(id_x)
