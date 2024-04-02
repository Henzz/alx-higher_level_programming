#!/bin/bash
# Takes in a URL and sends a GET request the displays the body of the response
curl -sb -X GET "$1"
#-o /dev/null -w "%{http_code}\n"
#"$1"
#| grep -q 200 && curl -s "$1"
