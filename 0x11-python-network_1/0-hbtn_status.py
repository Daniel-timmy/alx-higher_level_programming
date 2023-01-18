#!/usr/bin/python3
"""
a script that fetches
https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        page_reply = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(page_reply)))
        print('\t- content: {}'.format(page_reply))
        print('\t- utf8 content: {}'.format(page_reply.decode('utf-8')))
