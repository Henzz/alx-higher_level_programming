#!/usr/bin/python3
"""
Python script to send a request to a URL and display the value of
the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


def fetch_x(url):
    """
    Sends a request to the given URL and returns the value of the
    X-Request-Id variable in the response header.
    """
    with urllib.request.urlopen(url) as response:
        header = response.info()
        x_request_id = header.get('X-Request-Id')

    return x_request_id


if __name__ == "__main__":
    # Retrieve command-line argument
    url = sys.argv[1]
    x_request_id = fetch_x(url)

    print(x_request_id)
