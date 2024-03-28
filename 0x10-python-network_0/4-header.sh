#!/bin/bash
# Takes in a URL and sends a GET request to it with a header variable then displays the body of the response
curl -X GET -H "X-School-User-Id: 98" -s "$1"
