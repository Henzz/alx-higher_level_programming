#!/bin/bash
# Takes in a URL and sends a POST request to it then displays the body of the response
curl -sX POST "$1" -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"
