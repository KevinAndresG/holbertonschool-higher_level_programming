#!/bin/bash
# Bash script that sends a GET request to the URL
response=$(curl -s -I GET $1) | grep -i HTTP/ | awk '{if ($2 == 200) print "Route 2"}'
