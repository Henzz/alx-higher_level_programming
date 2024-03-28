#!/bin/bash
# Takes in a URL and sends a request then displays the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
