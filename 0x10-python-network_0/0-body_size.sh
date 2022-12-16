#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL
#  & displays the size of the body of the response in bytes using curl
curl "$1" | wc -c