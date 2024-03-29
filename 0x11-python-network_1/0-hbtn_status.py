#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status using urllib
"""
import urllib.request


def fetch():
    """
    Fetches url https://alx-intranet.hbtn.io/status
    """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")


if __name__ == "__main__":
    fetch()
