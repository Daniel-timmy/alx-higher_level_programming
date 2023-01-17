#!/usr/bin/python3
"""a script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    page_reply = response.read()

