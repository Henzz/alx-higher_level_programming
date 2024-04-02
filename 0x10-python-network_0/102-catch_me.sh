#!/bin/bash
# Takes in a URL and sends a request to it to get a message in the body response
curl -sX GET "$1" | exec 1>&2
