#!/usr/bin/python3
"""sends a POST request to the
passed URL with the email as a parameter
"""
import requests as requests
import sys


if __name__ == "__main__":
    dict_mail = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=dict_mail)
    print(response.text)
