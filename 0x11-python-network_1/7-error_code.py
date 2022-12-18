#!/usr/bin/python3
"""This takes a URL, sends requests to it & displays the body of the text"""

import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
