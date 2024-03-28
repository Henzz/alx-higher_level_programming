#!/bin/bash
# Takes in a URL and sends a request to it to get a message in the body response
curl -sX GET "$1" -d "You got me!"
