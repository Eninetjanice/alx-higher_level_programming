#!/bin/bash
# script that takes in a URL, sends GET and displays body of response
# Displays only body of a 200 status code response using curl
curl -sLX GET "$1"