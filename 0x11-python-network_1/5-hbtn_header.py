#!/usr/bin/python3
"""displays the value of the
variable X-Request-Id in the response header
"""
import requests as requests
import sys


if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        print(response.headers['X-Request-Id'])
    except:
        pass
