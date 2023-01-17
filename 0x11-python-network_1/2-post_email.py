#!/usr/bin/python3
"""a Python script that takes in a URL
and an email, sends a POST request"""

import urllib.request
import sys
if __name__ == "__main__":
    dict_mail = {'email': sys.argv[2]}
    query_string = urllib.parse.urlencode(dict_mail)
    data = query_string.encode("ascii")
    with urllib.request.urlopen(sys.argv[1], data) as response:
        response_text = response.read()
        print(response_text.decode('utf-8'))
