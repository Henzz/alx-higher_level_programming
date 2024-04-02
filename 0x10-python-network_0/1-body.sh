#!/bin/bash
# Takes in a URL and sends a GET request the displays the body of the response
response=$(curl -w '%{http_code}' -s -o /dev/null "$1"); [[ $response -eq 200 ]] && curl -s "$1"
