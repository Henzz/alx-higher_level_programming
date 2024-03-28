#!/bin/bash
# Takes in a URL and sends a DELETE request to it then displays the body of the response
curl -X DELETE -s "$1"
