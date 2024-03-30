#!/usr/bin/python3
"""
Python script to send a request to a URL and display the value of
the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import urllib.parse
import sys


def fetch(url):
    """
    Sends a request to the given URL and returns the bodt of the
    response (decoded in utf-8_.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
    else:
        return body


if __name__ == "__main__":
    # Retrieve command-line argument
    url = sys.argv[1]

    body = fetch(url)

    print(body)
