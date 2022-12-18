#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept
curl -s -H "X-School-User-Id: 98" -X GET "$1"
