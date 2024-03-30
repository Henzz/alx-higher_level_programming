#!/usr/bin/python3
"""
Python script to send a request to a URL and display the value of
the X-Request-Id variable found in the header of the response.
"""
import requests


def fetch(url):
    """
    Fetches the body response from the give URL using the
    requests package.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        body = response.text
        response_dict = {
                "type": type(body),
                "content": body
                }
        return response_dict
    except requests.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    # Retrieve command-line argument
    url = 'https://alx-intranet.hbtn.io/status'

    body = fetch(url)

    print("Body response:")
    for key, value in body.items:
        print(f"\t- {key}: {value}")
