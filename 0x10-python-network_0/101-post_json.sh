#!/bin/bash
# Takes in a URL and sends a POST request to it with a second argument of json file containing params then displays the body of the response
curl -sX POST "$1" -d "@$2" -H "Content-Type: application/json"
