#!/bin/bash
# Takes in a URL and sends a GET request the displays the body of the response
curl -sb -X GET "$1"
