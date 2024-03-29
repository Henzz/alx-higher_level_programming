#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status using urllib
"""
import urllib.request


def fetch(url):
    """
    Fetches url https://alx-intranet.hbtn.io/status
    """
    with urllib.request.urlopen(url) as response:
        body = response.read()

    response_dict = {
            "type": str(type(body)),
            "content": body,
            "utf8 content": body.decode('utf-8')
            }

    return response_dict


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    body = fetch(url)

    print("Body response:")
    for key, value in body.items():
        print(f"\t- {key}: {value}")
