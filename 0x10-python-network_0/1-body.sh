#!/bin/bash
# Takes in a URL and sends a GET request the displays the body of the response
curl -s -o /dev/null -w "%{http_code}\n" "$1" | grep -m1 200 && curl -s "$1"