#!/usr/bin/python3
"""
Python script to send a request to a URL and display the value of
the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import urllib.parse
import sys


def fetch_x(url, email):
    """
    Sends a request to the given URL and returns the value of the
    X-Request-Id variable in the response header.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')

    return body


if __name__ == "__main__":
    # Retrieve command-line argument
    url = sys.argv[1]
    email = sys.argv[2]

    body = fetch_x(url, email)

    print(body)
