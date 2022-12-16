#!/bin/bash
# This script takes in a URL, sends GET & displays 200 status code response body
curl -sLX GET "$1"
