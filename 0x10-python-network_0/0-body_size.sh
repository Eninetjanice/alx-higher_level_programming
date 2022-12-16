#!/bin/bash
# Script takes in a URL, sends request 2 it & displays body size in bytes
curl "$1" | wc -c
